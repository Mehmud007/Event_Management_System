# Generated by Django 2.2.6 on 2020-04-29 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventmanagement', '0003_hall_hall_rent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hall',
            name='hall_rent',
            field=models.FloatField(null='true'),
        ),
    ]