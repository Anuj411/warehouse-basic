# Generated by Django 5.0.7 on 2024-07-28 04:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_rename_order_created_by_orders_created_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='order_id',
            new_name='order_number',
        ),
    ]
