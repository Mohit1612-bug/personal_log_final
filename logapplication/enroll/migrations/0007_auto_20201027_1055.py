# Generated by Django 3.1.1 on 2020-10-27 05:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0006_auto_20201027_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 27, 10, 55, 4, 502288)),
        ),
    ]
