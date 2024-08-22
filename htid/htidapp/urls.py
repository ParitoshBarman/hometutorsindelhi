from django.contrib import admin
from django.urls import path
from htidapp import views



urlpatterns = [
    path("", views.index, name='home'),
    path("base", views.base, name='base'),
    path("about", views.about, name='about'),
    path("contact", views.contact, name='contact'),
    path("service", views.service, name='service'),
    path("teacher", views.teacher, name='teacher'),

    ]