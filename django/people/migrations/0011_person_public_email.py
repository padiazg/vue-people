# Generated by Django 2.0.4 on 2018-06-07 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0010_auto_20180413_0905'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='public_email',
            field=models.BooleanField(default=False),
        ),
    ]
