# Generated by Django 4.2.4 on 2023-11-25 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0021_signupdb_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipdb',
            name='Class',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='shipdb',
            name='Type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='shipdb',
            name='Volume',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]