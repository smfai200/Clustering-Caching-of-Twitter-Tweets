# Generated by Django 2.2.7 on 2019-12-27 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Caching', '0003_auto_20191226_2329'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='popularity',
            field=models.IntegerField(default=0.13436424411240122),
        ),
    ]