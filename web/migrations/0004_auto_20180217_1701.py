# Generated by Django 2.0.1 on 2018-02-17 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20180217_1657'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assistant',
            old_name='mail',
            new_name='email',
        ),
    ]
