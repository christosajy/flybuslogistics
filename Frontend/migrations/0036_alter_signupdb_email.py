# Generated by Django 4.2.4 on 2023-11-29 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0035_alter_signupdb_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signupdb',
            name='Email',
            field=models.CharField(default=True, max_length=100, unique=True),
        ),
    ]