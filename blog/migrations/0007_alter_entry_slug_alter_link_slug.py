# Generated by Django 5.0.1 on 2024-01-24 22:42
from __future__ import annotations

from django.db import migrations
from django.db import models


def forwards_func(apps, schema_editor):
    Entry = apps.get_model("blog", "Entry")
    Link = apps.get_model("blog", "Link")

    for entry in Entry.objects.all():
        if entry.slug and Entry.objects.filter(slug=entry.slug).count() > 1:
            entry.slug = f"{entry.slug}-{entry.id}"
            entry.save()
    for link in Link.objects.all():
        if link.slug and Link.objects.filter(slug=link.slug).count() > 1:
            link.slug = f"{link.slug}-{link.id}"
            link.save()


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0006_tag_description_alter_tag_name_alter_tag_slug"),
    ]

    operations = [
        migrations.RunPython(forwards_func, migrations.RunPython.noop),
        migrations.AlterField(
            model_name="entry",
            name="slug",
            field=models.SlugField(blank=True, max_length=75, unique=True),
        ),
        migrations.AlterField(
            model_name="link",
            name="slug",
            field=models.SlugField(blank=True, max_length=75, unique=True),
        ),
    ]
