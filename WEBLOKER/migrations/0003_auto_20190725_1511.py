# Generated by Django 2.2.3 on 2019-07-25 15:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('WEBLOKER', '0002_remove_lowongan_nama'),
    ]

    operations = [
        migrations.AddField(
            model_name='lowongan',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lowongan',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='perusahaan',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='perusahaan',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
