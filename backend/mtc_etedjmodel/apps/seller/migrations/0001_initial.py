# Generated by Django 2.2.3 on 2019-11-06 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(default='italy', max_length=60, null=True)),
                ('description', models.CharField(default='description', max_length=250, null=True)),
                ('latitude', models.FloatField(default=45.515904, null=True)),
                ('longitude', models.FloatField(default=9.21039, null=True)),
                ('image', models.FileField(unique=True, upload_to='scripts/')),
                ('verified', models.BooleanField(blank=True, default=False, null=True)),
                ('rating', models.FloatField(default=4, null=True)),
            ],
        ),
    ]
