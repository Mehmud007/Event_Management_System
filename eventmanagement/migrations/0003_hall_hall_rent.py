# Generated by Django 2.2.6 on 2020-04-29 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventmanagement', '0002_auto_20200423_1833'),
    ]

    operations = [
        migrations.AddField(
            model_name='hall',
            name='hall_rent',
            field=models.IntegerField(null='true'),
            preserve_default='true',
        ),
    ]
