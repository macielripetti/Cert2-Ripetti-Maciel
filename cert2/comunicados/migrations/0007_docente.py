# Generated by Django 4.2.13 on 2024-06-03 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comunicados', '0006_proyecto_remove_adminentidad_entidad_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=20, verbose_name='RUT')),
                ('nombre', models.CharField(max_length=20, verbose_name='Nombre')),
                ('titulo', models.CharField(max_length=50, verbose_name='Titulo')),
            ],
        ),
    ]
