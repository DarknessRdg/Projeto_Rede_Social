# Generated by Django 2.2.2 on 2019-07-15 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postagem', '0009_auto_20190715_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='texto',
            field=models.CharField(default=' ', max_length=255),
            preserve_default=False,
        ),
    ]