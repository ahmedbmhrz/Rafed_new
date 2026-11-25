from .models import ContactPage, SiteContactSettings, NavbarSettings

def site_settings(request):
    """
    Exposes unified site contact settings and navbar settings to all templates.
    First checks ContactPage (edited under Pages), then falls back to SiteContactSettings.
    """
    try:
        page = ContactPage.objects.first()
        contact = page if page else SiteContactSettings.get_settings()
        navbar = NavbarSettings.get_settings()
        return {
            'site_settings': contact,
            'navbar_settings': navbar,
        }
    except Exception:
        return {
            'site_settings': None,
            'navbar_settings': None,
        }

