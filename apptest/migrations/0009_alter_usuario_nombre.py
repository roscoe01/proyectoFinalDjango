# Generated by Django 4.1.3 on 2022-12-22 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apptest', '0008_alter_usuario_fechanacimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
    ]
