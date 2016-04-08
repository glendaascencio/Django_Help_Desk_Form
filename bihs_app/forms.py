from django.forms import ModelForm
from django import forms
from bihs_app.models import Ticket

software_choices = (
        ('soft_instalation', 'Instalation of a software such as Microsoft Words, Pages'),
        ('app_update', 'Application Update'),
        ('os_update', 'OS Update: Security Update'),
        ('virus_update', 'Virus Defenition Update such as semantic antivirus'),
        ('web_update', 'Web Plugging Updates: Flash'),
        ('security_update', 'Security Update'),
        ('instalation', 'Instalation of configuration or connections'),
)

hardware_choices = (
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
        ('troubleshooting_type', 'Troubleshooting smartboards, computer, sound'),
        ('instalation', 'Harware Instalation like doing the configuration or connections'),
)

class SoftwareForm(ModelForm):
    issue_type = forms.ChoiceField(
        choices= software_choices
    )

    class Meta:
        model = Ticket
        fields = '__all__'
        exclude = ('hardware_or_software',)



class HardwareForm(ModelForm):
    issue_type = forms.ChoiceField(
        choices= hardware_choices
    )

    class Meta:
        model = Ticket
        fields = '__all__'
        exclude = ('hardware_or_software',)
