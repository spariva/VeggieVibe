# Generated by Django 5.0.2 on 2024-02-13 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0002_alter_juego_pub_date_alter_juego_valoracion'),
    ]

    operations = [
        migrations.AddField(
            model_name='descripcion',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes/'),
        ),
    ]
