# Generated by Django 5.0.2 on 2024-02-13 17:14

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genero_text', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Juego',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('juego_text', models.CharField(max_length=30)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('valoracion', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10)])),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pagina.genero')),
            ],
        ),
        migrations.CreateModel(
            name='Descripcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion_text', models.TextField()),
                ('juego', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pagina.juego')),
            ],
        ),
    ]