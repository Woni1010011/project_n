# Generated by Django 4.2.5 on 2023-10-26 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contents_app', '0004_write_post'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Recipe',
        ),
    ]