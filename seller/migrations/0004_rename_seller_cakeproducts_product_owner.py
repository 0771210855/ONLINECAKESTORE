# Generated by Django 3.2.15 on 2023-01-06 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0003_alter_cakeproducts_seller'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cakeproducts',
            old_name='seller',
            new_name='product_owner',
        ),
    ]