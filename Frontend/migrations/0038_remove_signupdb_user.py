# Generated by Django 4.2.4 on 2023-12-01 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0037_signupdb_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signupdb',
            name='User',
        ),
    ]
