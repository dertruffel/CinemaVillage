# Generated by Django 3.2.5 on 2022-03-15 12:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0023_alter_event_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(blank=True, default=datetime.date(2022, 3, 15)),
        ),
    ]
