# Generated by Django 4.2.6 on 2023-11-28 05:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0029_testimonaialsdb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signupdb',
            name='Phone',
        ),
    ]
