# Generated by Django 4.1.3 on 2023-01-07 20:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apptest', '0017_rename_mensaje_mensaje_contenido_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mensaje',
            old_name='enviar',
            new_name='emisor',
        ),
        migrations.RenameField(
            model_name='mensaje',
            old_name='recibir',
            new_name='receptor',
        ),
    ]
