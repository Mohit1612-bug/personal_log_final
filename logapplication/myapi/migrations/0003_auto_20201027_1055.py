# Generated by Django 3.1.1 on 2020-10-27 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0002_hero_image_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hero',
            name='image_pic',
        ),
        migrations.AddField(
            model_name='hero',
            name='first_movie',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='hero',
            name='latest_movie',
            field=models.CharField(max_length=60, null=True),
        ),
    ]
