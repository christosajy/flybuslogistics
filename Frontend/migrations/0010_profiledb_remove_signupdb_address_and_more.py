# Generated by Django 4.2.4 on 2023-11-06 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0009_signupdb_address_signupdb_city_signupdb_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Email', models.CharField(blank=True, max_length=100, null=True)),
                ('Phone', models.CharField(blank=True, max_length=100, null=True)),
                ('Website', models.CharField(blank=True, max_length=100, null=True)),
                ('Address', models.TextField(blank=True, null=True)),
                ('City', models.CharField(blank=True, max_length=100, null=True)),
                ('State', models.CharField(blank=True, max_length=100, null=True)),
                ('Image', models.ImageField(blank=True, null=True, upload_to='pfofilepics')),
            ],
        ),
        migrations.RemoveField(
            model_name='signupdb',
            name='Address',
        ),
        migrations.RemoveField(
            model_name='signupdb',
            name='City',
        ),
        migrations.RemoveField(
            model_name='signupdb',
            name='Image',
        ),
        migrations.RemoveField(
            model_name='signupdb',
            name='Phone',
        ),
        migrations.RemoveField(
            model_name='signupdb',
            name='State',
        ),
        migrations.RemoveField(
            model_name='signupdb',
            name='Website',
        ),
    ]
