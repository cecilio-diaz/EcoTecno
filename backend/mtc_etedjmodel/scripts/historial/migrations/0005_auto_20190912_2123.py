# Generated by Django 2.2.3 on 2019-09-13 02:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('historial', '0004_auto_20190911_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estados',
            name='FechaTurno',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 12, 14, 30)),
        ),
        migrations.AlterField(
            model_name='estados_inicial',
            name='FechaTurno',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 12, 14, 30)),
        ),
    ]
