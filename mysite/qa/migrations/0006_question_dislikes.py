# Generated by Django 4.0 on 2022-01-28 12:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('qa', '0005_remove_question_thumbs_remove_question_thumbsdown_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='dislikes',
            field=models.ManyToManyField(blank=True, default=None, related_name='dislikes', to=settings.AUTH_USER_MODEL),
        ),
    ]
