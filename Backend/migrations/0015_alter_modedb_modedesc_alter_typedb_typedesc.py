# Generated by Django 4.2.4 on 2023-11-07 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0014_modedb_modeimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modedb',
            name='ModeDesc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='typedb',
            name='TypeDesc',
            field=models.TextField(blank=True, null=True),
        ),
    ]