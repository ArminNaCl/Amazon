# Generated by Django 3.1.4 on 2021-02-03 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20210203_1730'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagealbum',
            name='name',
            field=models.CharField(default='yes', max_length=60, verbose_name='name'),
        ),
    ]