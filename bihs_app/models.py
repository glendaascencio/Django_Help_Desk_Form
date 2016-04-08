from django.db import models

Who_Is_Requesting_Choices = (
    ('teacher', 'Teacher'),
    ('staff', 'Staff'),
)


what_type_of_request_do_you_need_help_with = (
    ('hardware', 'Hardware'),
    ('software', 'Software'),
)

all_choices = (
        ('projector', 'Projector'),
        ('pc_computer', 'PC Computer'),
        ('mac_computer', 'Mac Computer'),
        ('mobile_devices', 'Mobile Devices'),
        ('telephone', 'Telephone'),
        ('scanner', 'Scanner'),
        ('printer', 'Printer'),
        ('smartboard', 'Smartboard'),
        ('headphones', 'Headphones'),
        ('document_cameras', 'Document Cameras'),
        ('toner_replacement', 'Toner Replacement'),
        ('instalation', 'Harware Instalation like doing the configuration or connections'),

        ('soft_instalation', 'Instalation of a software such as Microsoft Words, Pages'),
        ('app_update', 'Application Update'),
        ('os_update', 'OS Update: Security Update'),
        ('virus_update', 'Virus Defenition Update such as semantic antivirus'),
        ('web_update', 'Web Plugging Updates: Flash'),
        ('security_update', 'Security Update'),
        ('troubleshooting_type', 'Troubleshooting smartboards, computer, sound'),
        ('smartboard', 'Smartboard'),
        ('headphones', 'Headphones'),
        ('document_cameras', 'Document Cameras'),
        ('toner_replacement', 'Toner Replacement'),
        ('instalation', 'Harware Instalation like doing the configuration or connections'),
)


class Ticket(models.Model):
    day = models.DateTimeField(
        auto_now_add=True,
        null = True
    )
    first_name = models.CharField(
        max_length=45
    )
    last_name = models.CharField(
        max_length=45,
        null = True
    )
    phone_number= models.IntegerField(
        default=1
    )
    email_address = models.EmailField(
        max_length=200,
        null = True
    )
    description = models.TextField(
        default='Description: '
    )
    staff_or_teacher = models.CharField(
        max_length=7,
        choices=Who_Is_Requesting_Choices,
        null=True
    )
    location = models.CharField(
        max_length=100, null=True
    )
    hardware_or_software = models.CharField(
        max_length=57,
        choices=what_type_of_request_do_you_need_help_with,
        null=True
    )
    issue_type = models.CharField(
        max_length=60,
        choices=all_choices,
        null=True
    )

