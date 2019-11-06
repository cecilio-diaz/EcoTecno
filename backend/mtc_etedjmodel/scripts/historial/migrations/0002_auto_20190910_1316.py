# Generated by Django 2.2.3 on 2019-09-10 18:16

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('DatosEmpresa', '0002_auto_20190910_1316'),
        ('estado_paros_deta3', '0001_initial'),
        ('historial', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estados',
            name='FechaTurno',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 10, 6, 30)),
        ),
        migrations.CreateModel(
            name='estados_inicial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('turno', models.FloatField(default=1)),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('fecha_creacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('FechaTurno', models.DateTimeField(default=datetime.datetime(2019, 9, 10, 6, 30))),
                ('Modo', models.CharField(blank=True, max_length=60, null=True)),
                ('Execution', models.CharField(blank=True, max_length=60, null=True)),
                ('Alarma', models.CharField(blank=True, max_length=60, null=True)),
                ('CorteViruta', models.BooleanField(blank=True, null=True)),
                ('deltaTime', models.FloatField(null=True)),
                ('maquina', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='DatosEmpresa.maquina')),
                ('paros_deta3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='estado_paros_deta3.paros_deta3')),
            ],
        ),
    ]
