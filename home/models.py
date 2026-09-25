from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

class HomePage(Page):
    hero_subheading = models.CharField(max_length=100, default="// The Best Bakery")
    hero_heading = models.CharField(max_length=100, default="We Bake With Passion")
    hero_text = models.CharField(max_length=255, default="Vero elitr justo clita lorem. Ipsum dolor sed stet sit diam rebum ipsum.")

    content_panels = Page.content_panels + [
        FieldPanel('hero_subheading'),
        FieldPanel('hero_heading'),
        FieldPanel('hero_text'),
    ]
