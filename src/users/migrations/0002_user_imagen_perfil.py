# Generated by Django 5.0 on 2023-12-28 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='imagen_perfil',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes_perfil'),
        ),
    ]
