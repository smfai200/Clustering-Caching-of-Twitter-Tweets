# Generated by Django 2.2.7 on 2019-12-27 16:17

import Caching.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Caching', '0007_remove_data_popularity'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='popularity',
            field=models.CharField(default=Caching.models.random_value, max_length=10),
        ),
    ]