# Generated by Django 2.2.6 on 2020-04-29 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventmanagement', '0005_auto_20200429_1603'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='selected_hotel',
        ),
        migrations.AddField(
            model_name='event',
            name='no_of_persons',
            field=models.IntegerField(null='true'),
            preserve_default='true',
        ),
    ]
