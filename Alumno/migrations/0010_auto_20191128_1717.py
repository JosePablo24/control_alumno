# Generated by Django 2.1.14 on 2019-11-28 23:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Alumno', '0009_auto_20191128_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='idCarrera',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Carrera.Carrera'),
        ),
    ]