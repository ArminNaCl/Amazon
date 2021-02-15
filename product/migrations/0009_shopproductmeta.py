# Generated by Django 3.1.4 on 2021-02-14 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_auto_20210212_1209'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopProductMeta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(choices=[('green', 'GREEN'), ('blue', 'BLUE'), ('red', 'RED'), ('orange', 'ORANGE'), ('black', 'BLACK')], default='green', max_length=6)),
                ('shop_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='metas', to='product.shopproduct', verbose_name='shop product')),
            ],
        ),
    ]