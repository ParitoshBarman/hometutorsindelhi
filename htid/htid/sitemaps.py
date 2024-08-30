from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

class StaticViewsSitemap(Sitemap):
    priority = 1.0
    changefreq = "daily"
    def items(self):
        return ['htidapp:home','htidapp:about','htidapp:contact', 'htidapp:service', 'htidapp:pricing', 'htidapp:classes', 'htidapp:termsandcondition', 'htidapp:privacypolicy']
    def location(self, item):
        return reverse(item)