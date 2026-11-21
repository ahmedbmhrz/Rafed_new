from django.contrib import admin
from .models import (
    ContactInquiry, SiteContactSettings
)

@admin.register(ContactInquiry)
class ContactInquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'subject', 'status', 'created_at', 'prefer_whatsapp')
    list_editable = ('status',)
    list_filter = ('status', 'subject', 'prefer_whatsapp', 'created_at')
    search_fields = ('name', 'phone', 'email', 'message')
    readonly_fields = ('name', 'phone', 'email', 'subject', 'message', 'prefer_whatsapp', 'created_at')

@admin.register(SiteContactSettings)
class SiteContactSettingsAdmin(admin.ModelAdmin):
    list_display = ('phone', 'email', 'address')
