# Generated by Django 2.2.3 on 2019-11-06 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='name',
            new_name='profile',
        ),
    ]
