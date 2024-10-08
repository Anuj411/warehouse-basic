# Generated by Django 5.0.7 on 2024-07-26 07:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.basemodel')),
                ('unique_id', models.CharField(max_length=255, unique=True)),
                ('status', models.CharField(choices=[('pen', 'Pending'), ('con', 'Confirmed'), ('dld', 'Delivered'), ('cnl', 'Canceled')], default='pen', max_length=50)),
                ('delevery_address', models.CharField(blank=True, max_length=255, null=True)),
            ],
            bases=('base.basemodel',),
        ),
        migrations.CreateModel(
            name='Orderitem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('items', models.ManyToManyField(related_name='order_item', to='products.product')),
            ],
        ),
    ]
