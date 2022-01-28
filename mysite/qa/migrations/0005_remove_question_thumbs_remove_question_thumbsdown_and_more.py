# Generated by Django 4.0 on 2022-01-28 07:35

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('qa', '0004_delete_vote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='thumbs',
        ),
        migrations.RemoveField(
            model_name='question',
            name='thumbsdown',
        ),
        migrations.RemoveField(
            model_name='question',
            name='thumbsup',
        ),
        migrations.AddField(
            model_name='question',
            name='likes',
            field=models.ManyToManyField(blank=True, default=None, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
