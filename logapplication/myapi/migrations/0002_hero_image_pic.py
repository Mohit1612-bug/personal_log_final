# Generated by Django 3.1.1 on 2020-09-27 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hero',
            name='image_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]