# Generated by Django 5.0.7 on 2024-07-28 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='weight',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
    ]
