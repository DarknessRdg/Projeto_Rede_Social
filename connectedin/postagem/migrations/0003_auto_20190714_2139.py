# Generated by Django 2.2.2 on 2019-07-14 21:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postagem', '0002_auto_20190714_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='data_post',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]