# Generated by Django 2.1.2 on 2018-10-20 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nasa_app', '0003_auto_20181020_2155'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='items',
            name='item_expiry_time',
        ),
    ]
