# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bihs_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='phone_number',
            field=models.IntegerField(default=0, max_length=11),
        ),
        migrations.AddField(
            model_name='ticket',
            name='request_type',
            field=models.CharField(max_length=1, null=True, choices=[(b'T', b'Teacher'), (b'S', b'Staff')]),
        ),
    ]
