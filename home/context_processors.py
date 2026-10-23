from .models import SiteContactSettings

def site_settings(request):
    """
    Exposes unified site contact settings to all templates.
    """
    try:
        settings_obj = SiteContactSettings.get_settings()
    except Exception:
        settings_obj = None
    return {
        'site_settings': settings_obj
    }
