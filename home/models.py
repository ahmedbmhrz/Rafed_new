from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel

class HomePage(Page):
    # Hero Section
    hero_subheading = models.CharField(max_length=100, default="جمعية رافد للأوقاف", verbose_name="العنوان الفرعي")
    hero_heading = models.CharField(max_length=100, default="نؤسس ونطور الأوقاف", verbose_name="العنوان الرئيسي")
    hero_text = models.CharField(max_length=255, default="جمعية تعنى بتأسيس وتطوير واستدامة الكيانات الوقفية.", verbose_name="النص")

    # Vision & Mission
    vision_title = models.CharField(max_length=100, default="رؤيتنا", verbose_name="عنوان الرؤية")
    vision_text = models.TextField(default="الريادة في تطوير واستدامة الأوقاف.", verbose_name="نص الرؤية")
    
    mission_title = models.CharField(max_length=100, default="رسالتنا", verbose_name="عنوان الرسالة")
    mission_text = models.TextField(default="تقديم خدمات متنوعة للراغبين في الوقف.", verbose_name="نص الرسالة")

    # Statistics
    stats_years = models.IntegerField(default=10, verbose_name="سنوات الخبرة")
    stats_projects = models.IntegerField(default=50, verbose_name="المشاريع الوقفية")
    stats_beneficiaries = models.IntegerField(default=10000, verbose_name="المستفيدين")

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('hero_subheading'),
            FieldPanel('hero_heading'),
            FieldPanel('hero_text'),
        ], heading="القسم الرئيسي (Hero)"),
        MultiFieldPanel([
            FieldPanel('vision_title'),
            FieldPanel('vision_text'),
            FieldPanel('mission_title'),
            FieldPanel('mission_text'),
        ], heading="الرؤية والرسالة"),
        MultiFieldPanel([
            FieldPanel('stats_years'),
            FieldPanel('stats_projects'),
            FieldPanel('stats_beneficiaries'),
        ], heading="الإحصائيات"),
    ]
