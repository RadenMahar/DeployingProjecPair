# Generated by Django 2.2.3 on 2019-07-25 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WEBLOKER', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lowongan',
            name='nama',
        ),
    ]