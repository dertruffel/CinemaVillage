# Generated by Django 3.2.5 on 2022-03-13 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
