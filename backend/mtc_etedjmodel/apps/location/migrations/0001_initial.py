# Generated by Django 2.2.3 on 2019-11-05 12:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_create', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('country', models.CharField(default='italy', max_length=60, null=True)),
                ('city', models.CharField(default='milano', max_length=60, null=True)),
                ('dataSource', models.CharField(blank=True, default='', max_length=60, null=True)),
                ('latitude', models.FloatField(default=45.515904, null=True)),
                ('longitude', models.FloatField(default=9.21039, null=True)),
                ('status', models.BooleanField(blank=True, default=True, null=True)),
                ('placesAvailable', models.IntegerField(default=2, null=True)),
                ('placesOccupied', models.IntegerField(default=2, null=True)),
                ('radius', models.IntegerField(default=1, null=True)),
            ],
        ),
    ]
