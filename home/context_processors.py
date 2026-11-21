from .models import ContactPage, SiteContactSettings

def site_settings(request):
    """
    Exposes unified site contact settings to all templates.
    First checks ContactPage (edited under Pages), then falls back to SiteContactSettings.
    """
    try:
        page = ContactPage.objects.first()
        if page:
            return {'site_settings': page}
        return {'site_settings': SiteContactSettings.get_settings()}
    except Exception:
        return {'site_settings': None}
