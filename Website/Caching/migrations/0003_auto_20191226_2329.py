# Generated by Django 2.2.7 on 2019-12-26 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Caching', '0002_auto_20191226_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='user_id',
            field=models.FloatField(),
        ),
    ]