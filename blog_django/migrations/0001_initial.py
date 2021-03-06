# Generated by Django 4.0.3 on 2022-03-19 13:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bloggero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('alias', models.CharField(max_length=30)),
                ('pais_de_residencia', models.CharField(max_length=30)),
                ('correo_electronico', models.EmailField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_de_empresa', models.CharField(max_length=30)),
                ('rubro', models.CharField(max_length=30)),
                ('cuit', models.PositiveIntegerField(verbose_name=django.core.validators.MaxValueValidator(30999999999))),
                ('correo_electronico', models.EmailField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Lector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_anonimo', models.CharField(max_length=30)),
                ('pais_de_residencia', models.CharField(max_length=30)),
                ('correo_electronico', models.EmailField(max_length=50)),
            ],
        ),
    ]
