# Generated by Django 3.2.15 on 2023-01-02 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('seller', '0001_initial'),
        ('userauthentications', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cakeproducts',
            name='seller',
            field=models.ForeignKey(default='1', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_Owner', to='userauthentications.seller'),
        ),
    ]
