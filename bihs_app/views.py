from django.shortcuts import render_to_response, render
from bihs_app.forms import SoftwareForm, HardwareForm

from django.http import HttpResponseRedirect

from bihs_app.models import Ticket
#from bihs_app.forms import softwarelist, hardwarelist

def home(request):
    alltickets = Ticket.objects.all()


    return render_to_response(
        "home.html",
        {"tickets": alltickets}
    )


def softwareTicket(request):
    #IF someone submits the button, we receive and POST method in the request
    # Basically they submitted the form
    if request.method =='POST':
        form = SoftwareForm(request.POST)
        if form.is_valid():
            Ticket = form.save(commit=False)
            Ticket.hardware_or_software = 'software'
            Ticket.save()
            return HttpResponseRedirect('/')

    else:
        #Putting the forms inside the view python file
        form = SoftwareForm()

    return render(
        request,
        "softwareticket.html",
        {
            "formInHTML": form,
        }
    )

def hardwareTicket(request):
    #IF someone submits the button, we receive and POST method in the request
    # Basically they submitted the form
    if request.method =='POST':
        form = HardwareForm(request.POST)
        if form.is_valid():
            Ticket = form.save(commit=False)
            Ticket.hardware_or_software = 'hardware'
            Ticket.save()
            return HttpResponseRedirect('/')

    else:
        #Putting the forms inside the view python file
        form = HardwareForm()
        return render(
        request,
        "softwareticket.html",
        {
            "formInHTML": form,
        }
    )

    return render(
        request,
        "hardwareticket.html",
        {
            "formInHTML": form,
        }
    )

def hardwareList(request):
    return render_to_response(
        "hardwarelist.html"
    )

def softwareList(request):
    return render_to_response(
        "softwarelist.html"
    )