# Generated by Django 3.1.4 on 2021-02-16 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_auto_20210215_1500'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='condition',
        ),
        migrations.AlterField(
            model_name='like',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like_product', to='product.shopproduct', verbose_name='item'),
        ),
    ]