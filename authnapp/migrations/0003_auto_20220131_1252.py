# Generated by Django 3.2.10 on 2022-01-31 09:52

import datetime

from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ("authnapp", "0002_auto_20220128_1419"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shopuser",
            name="activation_key_expires",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 2, 2, 9, 52, 51, 623587, tzinfo=utc), verbose_name="актуальность ключа"
            ),
        ),
        migrations.AlterField(
            model_name="shopuser",
            name="age",
            field=models.PositiveIntegerField(default=18, verbose_name="возраст"),
        ),
    ]
