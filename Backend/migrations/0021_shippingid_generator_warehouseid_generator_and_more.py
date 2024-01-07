# Generated by Django 4.2.4 on 2023-11-24 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0020_trackingdb_storageid'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShippingID_Generator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TrackingId', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WarehouseID_Generator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StorageId', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='TrackingDB',
        ),
    ]
