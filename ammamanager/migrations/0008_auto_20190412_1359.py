# Generated by Django 2.1.4 on 2019-04-12 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ammamanager', '0007_fighter_rank'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bout',
            old_name='final',
            new_name='set',
        ),
    ]
