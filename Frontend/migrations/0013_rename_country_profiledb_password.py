# Generated by Django 4.2.4 on 2023-11-11 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0012_remove_profiledb_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profiledb',
            old_name='Country',
            new_name='Password',
        ),
    ]