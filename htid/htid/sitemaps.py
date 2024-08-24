from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

class StaticViewsSitemap(Sitemap):
    priority = 1.0
    changefreq = "daily"
    def items(self):
        return ['htidapp:home','htidapp:about','htidapp:contact']
    def location(self, item):
        return reverse(item)