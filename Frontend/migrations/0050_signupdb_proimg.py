# Generated by Django 4.2.4 on 2023-12-22 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0049_alter_signupdb_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='signupdb',
            name='ProImg',
            field=models.ImageField(blank=True, null=True, upload_to='profile'),
        ),
    ]
