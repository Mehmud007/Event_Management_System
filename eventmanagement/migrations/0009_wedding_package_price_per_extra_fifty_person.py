# Generated by Django 2.2.6 on 2020-05-06 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventmanagement', '0008_auto_20200505_1624'),
    ]

    operations = [
        migrations.AddField(
            model_name='wedding_package',
            name='Price_per_extra_fifty_person',
            field=models.FloatField(null='true'),
            preserve_default='true',
        ),
    ]