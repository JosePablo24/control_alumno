# Generated by Django 2.1.14 on 2019-11-28 23:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Alumno', '0007_auto_20191128_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='idCarrera',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Carrera.Carrera'),
        ),
    ]