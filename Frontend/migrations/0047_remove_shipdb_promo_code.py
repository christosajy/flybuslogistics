# Generated by Django 4.2.4 on 2023-12-16 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0046_rename_from_date_shipdb_from_address_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shipdb',
            name='Promo_Code',
        ),
    ]
