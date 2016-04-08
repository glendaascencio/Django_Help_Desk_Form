# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bihs_app', '0003_auto_20150829_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='first_name',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='hardware_support',
            field=models.CharField(max_length=60, null=True, choices=[(b'projector', b'Projector'), (b'pc_computer', b'PC Computer'), (b'mac_computer', b'Mac Computer'), (b'mobile_devices', b'Mobile Devices'), (b'telephone', b'Telephone'), (b'scanner', b'Scanner'), (b'printer', b'Printer'), (b'smartboard', b'Smartboard'), (b'headphones', b'Headphones'), (b'document_cameras', b'Document Cameras'), (b'toner_replacement', b'Toner Replacement'), (b'instalation', b'Harware Instalation like doing the configuration or connections')]),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='last_name',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='location_issue',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='request_type',
            field=models.CharField(max_length=7, null=True, choices=[(b'teacher', b'Teacher'), (b'staff', b'Staff')]),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='software_support',
            field=models.CharField(max_length=60, null=True, choices=[(b'soft_instalation', b'Instalation of a software such as Microsoft Words, Pages'), (b'app_update', b'Application Update'), (b'os_update', b'OS Update: Security Update'), (b'virus_update', b'Virus Defenition Update such as semantic antivirus'), (b'web_update', b'Web Plugging Updates: Flash'), (b'security_update', b'Security Update'), (b'troubleshooting_type', b'Troubleshooting smartboards, computer, sound'), (b'smartboard', b'Smartboard'), (b'headphones', b'Headphones'), (b'document_cameras', b'Document Cameras'), (b'toner_replacement', b'Toner Replacement'), (b'instalation', b'Harware Instalation such as doing the configuration and the connections')]),
        ),
    ]
