# Generated by Django 3.1.4 on 2021-02-15 15:00

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_ofer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percent', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(99)], verbose_name='percent')),
                ('expire', models.BooleanField(default=False, verbose_name='expire')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Create at')),
                ('expire_at', models.DateTimeField(verbose_name='expire date')),
                ('shop_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='offers', related_query_name='offers', to='product.shopproduct', verbose_name='shop product')),
            ],
            options={
                'verbose_name': 'Offer',
                'verbose_name_plural': 'Offers',
                'ordering': ['-create_at'],
            },
        ),
        migrations.DeleteModel(
            name='Ofer',
        ),
    ]
