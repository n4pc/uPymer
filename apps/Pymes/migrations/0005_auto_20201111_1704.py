# Generated by Django 3.1.2 on 2020-11-11 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pymes', '0004_auto_20201031_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='img',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pyme',
            name='img',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
