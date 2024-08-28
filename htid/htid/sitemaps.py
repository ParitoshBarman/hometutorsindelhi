from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

class StaticViewsSitemap(Sitemap):
    priority = 1.0
    changefreq = "daily"
    def items(self):
        return ['htidapp:home','htidapp:about','htidapp:contact', 'htidapp:privacypolicy', 'htidapp:termsandcondition']
    def location(self, item):
        return reverse(item)