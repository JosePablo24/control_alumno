# Generated by Django 2.2.7 on 2019-11-29 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Alumno', '0011_auto_20191128_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='idCarrera',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Carrera.Carrera'),
        ),
    ]
