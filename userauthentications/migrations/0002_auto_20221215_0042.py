# Generated by Django 3.2.15 on 2022-12-14 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauthentications', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='fullname',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='password',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='username',
            field=models.CharField(db_index=True, max_length=20, null=True, unique=True),
        ),
    ]