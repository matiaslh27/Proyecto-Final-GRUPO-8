# Generated by Django 5.0 on 2023-12-29 23:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicaciones', '0005_publicacion_me_gusta'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='me_gusta',
            field=models.ManyToManyField(blank=True, related_name='posts', to=settings.AUTH_USER_MODEL),
        ),
    ]