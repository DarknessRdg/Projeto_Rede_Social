# Generated by Django 2.2.2 on 2019-07-14 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postagem', '0003_auto_20190714_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='texto',
            field=models.TextField(blank=True),
        ),
    ]