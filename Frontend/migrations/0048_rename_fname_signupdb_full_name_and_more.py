# Generated by Django 4.2.4 on 2023-12-18 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0047_remove_shipdb_promo_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signupdb',
            old_name='FName',
            new_name='Full_Name',
        ),
        migrations.RemoveField(
            model_name='signupdb',
            name='LName',
        ),
    ]
