# Generated by Django 3.1 on 2020-10-13 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_auto_20201013_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='bid',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='listing',
            name='starting_bid',
            field=models.IntegerField(),
        ),
    ]
