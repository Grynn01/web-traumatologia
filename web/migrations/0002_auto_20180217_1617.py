# Generated by Django 2.0.1 on 2018-02-17 16:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assistant',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
