# Generated by Django 2.1 on 2023-03-03 15:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 3, 15, 59, 23, 186760, tzinfo=utc)),
        ),
    ]
