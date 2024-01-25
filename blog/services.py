from __future__ import annotations

from django.http import HttpRequest
from django.utils import timezone

from core.date_utils import get_range_between_dates

from .models import Entry
from .models import Link


class PostService:
    @classmethod
    def get_posts(
        cls, request: HttpRequest
    ) -> tuple[list[dict[str, Entry | Link]], object]:
        page_number = request.GET.get("page")

        entries = (
            Entry.objects.for_user(request.user)
            .prefetch_related("tags")
            .reverse_chronological()
        )

        page_obj = entries.paginated(page_number=page_number)

        start_date = page_obj.start_date
        end_date = page_obj.end_date
        # if there's only one page, we want to show all posts
        # once there's more than one page, we can just change this to
        # check if page_number == "1" only
        if start_date == end_date or page_number == "1":
            start_date = timezone.now()

        date_range = get_range_between_dates(start_date, end_date)
        print("date_range", date_range)

        links = list(
            Link.objects.filter(
                published_at__date__range=[date_range[-1].date(), date_range[0].date()]
            )
            .prefetch_related("tags")
            .order_by("-created_at")
        )
        print("links", links)

        dated_items = []
        for date in date_range:
            items = []
            for link in links:
                if link.published_at and link.published_at.date() == date.date():
                    items.append({"type": "link", "entry": link})
            for entry in page_obj.object_list:
                if entry.published_at and entry.published_at.date() == date.date():
                    items.append({"type": "entry", "entry": entry})
            dated_items.append({"date": date, "items": items})
            print("dated_items", {"date": date, "items": items})

        return dated_items, page_obj
