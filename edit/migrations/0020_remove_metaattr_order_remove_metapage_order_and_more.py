# Generated by Django 4.2.4 on 2023-12-17 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edit', '0019_qgame_subversion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='metaattr',
            name='order',
        ),
        migrations.RemoveField(
            model_name='metapage',
            name='order',
        ),
        migrations.RemoveField(
            model_name='metapage',
            name='params',
        ),
        migrations.RemoveField(
            model_name='metapage',
            name='return_type',
        ),
    ]
