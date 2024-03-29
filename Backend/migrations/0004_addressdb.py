# Generated by Django 4.2.6 on 2023-10-31 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0003_typedb'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddressDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Address', models.TextField(blank=True, max_length=100, null=True)),
                ('IDNumber', models.IntegerField(blank=True, null=True)),
                ('Phone', models.IntegerField(blank=True, null=True)),
                ('Email', models.EmailField(blank=True, max_length=100, null=True)),
                ('Website', models.URLField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
