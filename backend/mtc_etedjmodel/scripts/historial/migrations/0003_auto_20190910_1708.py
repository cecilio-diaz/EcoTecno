# Generated by Django 2.2.3 on 2019-09-10 22:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('historial', '0002_auto_20190910_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estados',
            name='FechaTurno',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 10, 14, 30)),
        ),
        migrations.AlterField(
            model_name='estados',
            name='turno',
            field=models.FloatField(default=2),
        ),
        migrations.AlterField(
            model_name='estados_inicial',
            name='FechaTurno',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 10, 14, 30)),
        ),
        migrations.AlterField(
            model_name='estados_inicial',
            name='turno',
            field=models.FloatField(default=2),
        ),
    ]
