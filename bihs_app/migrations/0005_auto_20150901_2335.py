# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bihs_app', '0004_auto_20150829_0022'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='location_issue',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='ticket',
            old_name='request_type',
            new_name='staff_or_teacher',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='hardware_support',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='software_support',
        ),
        migrations.AddField(
            model_name='ticket',
            name='day',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='email_address',
            field=models.EmailField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='hardware_or_software',
            field=models.CharField(max_length=57, null=True, choices=[(b'hardware', b'Hardware'), (b'software', b'Software')]),
        ),
        migrations.AddField(
            model_name='ticket',
            name='issue_tyoe',
            field=models.CharField(max_length=60, null=True, choices=[(b'projector', b'Projector'), (b'pc_computer', b'PC Computer'), (b'mac_computer', b'Mac Computer'), (b'mobile_devices', b'Mobile Devices'), (b'telephone', b'Telephone'), (b'scanner', b'Scanner'), (b'printer', b'Printer'), (b'smartboard', b'Smartboard'), (b'headphones', b'Headphones'), (b'document_cameras', b'Document Cameras'), (b'toner_replacement', b'Toner Replacement'), (b'instalation', b'Harware Instalation like doing the configuration or connections'), (b'soft_instalation', b'Instalation of a software such as Microsoft Words, Pages'), (b'app_update', b'Application Update'), (b'os_update', b'OS Update: Security Update'), (b'virus_update', b'Virus Defenition Update such as semantic antivirus'), (b'web_update', b'Web Plugging Updates: Flash'), (b'security_update', b'Security Update'), (b'troubleshooting_type', b'Troubleshooting smartboards, computer, sound'), (b'smartboard', b'Smartboard'), (b'headphones', b'Headphones'), (b'document_cameras', b'Document Cameras'), (b'toner_replacement', b'Toner Replacement'), (b'instalation', b'Harware Instalation like doing the configuration or connections')]),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='last_name',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='phone_number',
            field=models.IntegerField(default=1),
        ),
    ]
