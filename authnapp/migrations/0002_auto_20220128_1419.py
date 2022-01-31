# Generated by Django 3.2.10 on 2022-01-28 11:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authnapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopuser',
            name='activation_key',
            field=models.CharField(blank=True, max_length=128, verbose_name='ключ подтверждения'),
        ),
        migrations.AddField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 30, 11, 19, 41, 148399, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]
