# Generated by Django 3.1.4 on 2021-02-11 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20210206_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmeta',
            name='value',
            field=models.CharField(max_length=60, verbose_name='value'),
        ),
    ]