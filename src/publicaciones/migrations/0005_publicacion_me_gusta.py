# Generated by Django 5.0 on 2023-12-29 23:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicaciones', '0004_comentario'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacion',
            name='me_gusta',
            field=models.ManyToManyField(null=True, related_name='posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
