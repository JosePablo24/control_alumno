# Generated by Django 2.1.14 on 2019-11-26 01:12

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Carrera', '0002_auto_20191125_1912'),
        ('Alumno', '0002_auto_20191125_1912'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlumnoCarreras',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delete', models.BooleanField(default=False)),
                ('create', models.DateTimeField(default=django.utils.timezone.localtime)),
                ('idAlumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Alumno.Alumno')),
                ('idCarrera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Carrera.Carrera')),
            ],
            options={
                'db_table': 'AlumnoCarreras',
            },
        ),
    ]