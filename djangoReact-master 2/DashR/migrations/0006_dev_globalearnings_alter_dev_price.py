# Generated by Django 4.1.3 on 2022-12-02 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DashR', '0005_project_isover'),
    ]

    operations = [
        migrations.AddField(
            model_name='dev',
            name='globalEarnings',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='dev',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
