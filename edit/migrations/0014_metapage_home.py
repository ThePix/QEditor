# Generated by Django 4.2.1 on 2023-11-10 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edit', '0013_metapage_alias'),
    ]

    operations = [
        migrations.AddField(
            model_name='metapage',
            name='home',
            field=models.BooleanField(default=False),
        ),
    ]
