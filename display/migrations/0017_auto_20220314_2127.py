# Generated by Django 3.2.5 on 2022-03-14 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0016_event_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.CharField(max_length=255),
        ),
    ]