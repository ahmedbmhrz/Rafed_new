from django.contrib import admin
from .models import (
    SiteContactSettings, AchievementMetric, NewsItem, 
    EducationalDesign, ProjectItem, TeamMember, 
    TestimonialItem, ContactInquiry, VideoItem
)

@admin.register(SiteContactSettings)
class SiteContactSettingsAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'phone', 'email', 'address')

@admin.register(AchievementMetric)
class AchievementMetricAdmin(admin.ModelAdmin):
    list_display = ('title', 'number', 'unit', 'order', 'is_active')
    list_editable = ('number', 'unit', 'order', 'is_active')
    search_fields = ('title',)

@admin.register(NewsItem)
class NewsItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_text', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    search_fields = ('title', 'excerpt')

@admin.register(EducationalDesign)
class EducationalDesignAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_text', 'badge_text', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    search_fields = ('title',)

@admin.register(ProjectItem)
class ProjectItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'status', 'progress_percentage', 'is_featured', 'order')
    list_editable = ('status', 'progress_percentage', 'is_featured', 'order')
    list_filter = ('category', 'status', 'is_featured')
    search_fields = ('title', 'description')

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'category', 'order', 'is_active')
    list_editable = ('role', 'category', 'order', 'is_active')
    list_filter = ('category', 'is_active')
    search_fields = ('name', 'role', 'bio')

@admin.register(TestimonialItem)
class TestimonialItemAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'author_title', 'organization', 'rating', 'order', 'is_featured')
    list_editable = ('order', 'is_featured')
    list_filter = ('rating', 'is_featured')
    search_fields = ('author_name', 'author_title', 'quote')

@admin.register(ContactInquiry)
class ContactInquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'subject', 'status', 'created_at', 'prefer_whatsapp')
    list_editable = ('status',)
    list_filter = ('status', 'subject', 'prefer_whatsapp', 'created_at')
    search_fields = ('name', 'phone', 'email', 'message')
    readonly_fields = ('name', 'phone', 'email', 'subject', 'message', 'prefer_whatsapp', 'created_at')

@admin.register(VideoItem)
class VideoItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_text', 'duration', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    search_fields = ('title',)
