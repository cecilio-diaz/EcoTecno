# Generated by Django 2.2.3 on 2019-11-06 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0002_auto_20191106_0838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.CharField(default='description', max_length=250, null=True),
        ),
    ]