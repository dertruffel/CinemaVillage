# Generated by Django 3.2.5 on 2022-03-14 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0004_ticket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]