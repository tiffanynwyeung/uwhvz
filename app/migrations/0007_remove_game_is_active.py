# Generated by Django 2.0.2 on 2018-03-20 03:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20180319_0619'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='is_active',
        ),
    ]
