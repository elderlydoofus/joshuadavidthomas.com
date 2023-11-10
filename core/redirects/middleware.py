from __future__ import annotations

from django.conf import settings
from django.http import HttpResponse


def redirect_middleware(get_response):
    def middleware(request):
        redirect = settings.REDIRECTS.get_redirect(request)

        if redirect:
            response = HttpResponse(status=redirect.status)
            response["Location"] = redirect.destination_url
        else:
            response = get_response(request)

        return response

    return middleware
