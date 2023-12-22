# Generated by Django 5.0 on 2023-12-22 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicaciones', '0002_categoria_alter_publicacion_creador_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacion',
            name='imagen',
            field=models.ImageField(blank=True, upload_to='imagen-post'),
        ),
        migrations.AddField(
            model_name='publicacion',
            name='link_compra',
            field=models.TextField(blank=True, null=True),
        ),
    ]
