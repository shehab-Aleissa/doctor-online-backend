# Generated by Django 2.1.1 on 2018-09-28 23:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20180928_2248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctorprofile',
            name='scheduel',
        ),
    ]