# Generated by Django 2.2.3 on 2019-11-06 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['product']},
        ),
        migrations.RenameField(
            model_name='seller_product',
            old_name='Product',
            new_name='Products',
        ),
        migrations.AddField(
            model_name='seller_product',
            name='test',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
    ]