# Generated by Django 2.2.2 on 2019-07-15 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfis', '0002_perfil_is_active'),
        ('postagem', '0008_auto_20190715_1339'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='reacao',
            unique_together={('post', 'perfil')},
        ),
    ]