# Generated by Django 5.0.6 on 2024-05-23 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_entry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publishedentry',
            name='summary',
            field=models.TextField(blank=True),
        ),
    ]
