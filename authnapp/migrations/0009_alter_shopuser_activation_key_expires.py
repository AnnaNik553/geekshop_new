# Generated by Django 3.2.10 on 2022-02-12 13:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authnapp', '0008_alter_shopuser_activation_key_expires'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 14, 13, 36, 45, 4868, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]
