# Generated by Django 4.0.4 on 2023-02-15 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('integra', '0005_departamento_publicaciones_dep'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicaciones',
            name='banner',
            field=models.ImageField(blank=True, upload_to='vacante'),
        ),
    ]