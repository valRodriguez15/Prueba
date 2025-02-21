# Generated by Django 5.1.6 on 2025-02-21 20:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('detalle', models.TextField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(20000.0), django.core.validators.MaxValueValidator(90000.0)])),
                ('horario', models.CharField(max_length=100)),
                ('edadMin', models.CharField(max_length=30)),
                ('miniature', models.ImageField(blank=True, null=True, upload_to='categories/img/')),
            ],
        ),
        migrations.CreateModel(
            name='Tours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('descripcion', models.TextField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(60000.0), django.core.validators.MaxValueValidator(300000.0)])),
                ('disponibilidad', models.BooleanField(default=True)),
                ('ubicacion', models.CharField(max_length=200)),
            ],
        ),
    ]
