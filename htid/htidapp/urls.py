from django.contrib import admin
from django.urls import path
from htidapp import views
from django.contrib.sitemaps.views import sitemap
from htid.sitemaps import StaticViewsSitemap

sitemaps = {
    'sitemap': StaticViewsSitemap
}



urlpatterns = [
    path("", views.index, name='home'),
    path("base", views.base, name='base'),
    path("about", views.about, name='about'),
    path("contact", views.contact, name='contact'),
    path("service", views.service, name='service'),
    path("teacher", views.teacher, name='teacher'),
    path("privacypolicy", views.privacypolicy, name='privacypolicy'),
    path("termsandcondition", views.termsandcondition, name='termsandcondition'),
    path("pricing", views.pricing, name='pricing'),
    path("classes", views.classes, name='classes'),
    path("webhook", views.webhook, name='webhook'),

    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="django.contrib.sitemaps.views.sitemap"),

    ]