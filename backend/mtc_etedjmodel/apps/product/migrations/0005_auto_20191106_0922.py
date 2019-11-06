# Generated by Django 2.2.3 on 2019-11-06 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0002_auto_20191106_0838'),
        ('product', '0004_auto_20191106_0919'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seller_product',
            name='test',
        ),
        migrations.AddField(
            model_name='seller_product',
            name='seller',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='seller.profile'),
        ),
    ]
