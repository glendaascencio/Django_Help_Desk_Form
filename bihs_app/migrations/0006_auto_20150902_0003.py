# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bihs_app', '0005_auto_20150901_2335'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='issue_tyoe',
            new_name='issue_type',
        ),
    ]
