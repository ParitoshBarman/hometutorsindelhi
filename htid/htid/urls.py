from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Home Tutors in Delhi Admin"
admin.site.site_title = "Home Tutors in Delhi Admin Portal"
admin.site.index_title = "Welcome to Home Tutors in Delhi Portal"


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('htidapp.urls'))
    path('', include(('htidapp.urls', 'htidapp'), namespace='htidapp')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_URL)