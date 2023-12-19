from django.contrib import admin
from .models import SendContact

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'subject',
    )

admin.site.register(SendContact, ContactAdmin)