# Generated by Django 4.2.4 on 2023-11-25 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0024_rename_shippingid_shipdb_shipping_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='StorageGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Order_Status', models.CharField(blank=True, max_length=100, null=True)),
                ('Weightage', models.CharField(blank=True, max_length=100, null=True)),
                ('Class', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]