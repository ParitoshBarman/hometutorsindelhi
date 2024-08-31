from django.contrib import admin
from htidapp.models import ContactMessage
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class ContactMessageClass(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("fullname", "email", "phone", "subject", "msgTime", "msgdate")

admin.site.register(ContactMessage, ContactMessageClass)