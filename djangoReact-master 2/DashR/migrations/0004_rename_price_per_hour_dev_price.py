# Generated by Django 4.1.3 on 2022-11-21 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DashR', '0003_dev_firstname_dev_lastname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dev',
            old_name='price_per_hour',
            new_name='price',
        ),
    ]