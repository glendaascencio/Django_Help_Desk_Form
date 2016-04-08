# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bihs_app', '0006_auto_20150902_0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='email_address',
            field=models.EmailField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='first_name',
            field=models.CharField(max_length=45),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='last_name',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='location',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
