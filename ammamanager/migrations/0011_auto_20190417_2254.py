# Generated by Django 2.1.3 on 2019-04-17 21:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ammamanager', '0010_event_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='finished',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 4, 17, 22, 54, 28, 782796)),
        ),
    ]
