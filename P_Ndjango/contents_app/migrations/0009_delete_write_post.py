# Generated by Django 4.2.5 on 2023-10-30 21:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contents_app', '0008_board_post_hit'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Write_post',
        ),
    ]