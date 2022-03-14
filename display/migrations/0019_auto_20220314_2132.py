# Generated by Django 3.2.5 on 2022-03-14 20:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('display', '0018_alter_event_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='like',
            field=models.ManyToManyField(default=None, related_name='like', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.CharField(default=None, max_length=255),
        ),
    ]
