# Generated by Django 2.2.6 on 2020-05-06 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventmanagement', '0009_wedding_package_price_per_extra_fifty_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wedding_package',
            name='Price_per_extra_fifty_person',
            field=models.FloatField(),
        ),
    ]