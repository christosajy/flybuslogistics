# Generated by Django 4.2.4 on 2023-10-26 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TrackingDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TrackingID', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
