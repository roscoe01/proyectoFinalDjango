# Generated by Django 4.1.3 on 2022-12-22 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apptest', '0012_rename_corredor_piloto'),
    ]

    operations = [
        migrations.AddField(
            model_name='piloto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='img'),
        ),
    ]