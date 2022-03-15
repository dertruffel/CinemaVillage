# Generated by Django 3.2.5 on 2022-03-15 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0020_alter_event_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.CharField(blank=True, default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, default=None, upload_to=''),
        ),
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.CharField(blank=True, default=None, max_length=255),
        ),
    ]