# Generated by Django 2.0.6 on 2018-07-02 03:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_announcementpage_gameinfopage_missionpage'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SignupToken',
            new_name='SignupInvite',
        ),
    ]