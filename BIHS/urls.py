"""BIHS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'bihs_app.views.home', name='home'),
    url(r'^hardwareticket', 'bihs_app.views.hardwareTicket', name = 'hardwareTicket'),
    url(r'^softwareticket', 'bihs_app.views.softwareTicket', name = 'softwareTicket'),
    url(r'^hardwarelist', 'bihs_app.views.hardwareList', name = 'hardwareList'),
    url(r'^softwarelist', 'bihs_app.views.softwareList', name = 'softwareList'),

]
