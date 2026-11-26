from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from wagtail import hooks
from wagtail.admin.menu import MenuItem, SubmenuMenuItem, Menu
from wagtail.admin.ui.sidebar import PageExplorerMenuItem as PageExplorerMenuItemComponent
from wagtail.models import Page
from home.models import (
    HomePage, AboutPage, ServicesPage, ProjectsPage, 
    TeamPage, TestimonialsPage, VideosPage, ContactPage,
    NavbarSettings, CareersPage
)


# ==============================================================================
# 1. CUSTOMIZE PAGES EXPLORER FLYOUT
# Makes the Pages flyout open directly at Home (listing all pages individually)
# instead of Root (which only showed "Home").
# ==============================================================================

class SitePagesExplorerMenuItem(MenuItem):
    def is_shown(self, request):
        return request.user.has_perm("wagtailadmin.access_admin")

    def render_component(self, request):
        home = HomePage.objects.first()
        start_id = home.id if home else 1
        url = reverse("wagtailadmin_explore", args=[start_id])
        return PageExplorerMenuItemComponent(
            self.name,
            self.label,
            url,
            start_id,
            icon_name=self.icon_name,
            classname=self.classname,
        )


@hooks.register("construct_main_menu")
def customize_main_menu(request, menu_items):
    # Replace default explorer item with our custom one starting at Home
    home = HomePage.objects.first()
    start_id = home.id if home else 1

    for i, item in enumerate(menu_items):
        if item.name == "explorer":
            menu_items[i] = SitePagesExplorerMenuItem(
                _("Pages"),
                reverse("wagtailadmin_explore", args=[start_id]),
                name="explorer",
                icon_name="folder-open-inverse",
                order=item.order,
            )
            break


# ==============================================================================
# 2. DEDICATED DIRECT ACCESS TO ALL PAGES IN ADMIN SIDEBAR
# ==============================================================================

class DynamicPageEditMenuItem(MenuItem):
    def __init__(self, name, label, model_class, icon_name, order):
        self.model_class = model_class
        self._url = "#"
        super().__init__(label, "#", name=name, icon_name=icon_name, order=order)

    @property
    def url(self):
        page = self.model_class.objects.first()
        if page:
            return reverse("wagtailadmin_pages:edit", args=[page.id])
        return self._url

    @url.setter
    def url(self, value):
        self._url = value


# Custom Submenu for Site Pages
pages_edit_menu = Menu(
    register_hook_name="register_pages_edit_menu_item",
    construct_hook_name="construct_pages_edit_menu",
)

@hooks.register("register_admin_menu_item")
def register_pages_edit_submenu():
    return SubmenuMenuItem(
        "تعديل الصفحات",
        pages_edit_menu,
        name="pages_edit",
        icon_name="doc-full-inverse",
        order=110,
    )


@hooks.register("register_pages_edit_menu_item")
def register_home_page_item():
    return DynamicPageEditMenuItem("page_home", "الرئيسية", HomePage, "home", 10)

@hooks.register("register_pages_edit_menu_item")
def register_about_page_item():
    return DynamicPageEditMenuItem("page_about", "من نحن", AboutPage, "info-circle", 20)

@hooks.register("register_pages_edit_menu_item")
def register_services_page_item():
    return DynamicPageEditMenuItem("page_services", "خدماتنا", ServicesPage, "cogs", 30)

@hooks.register("register_pages_edit_menu_item")
def register_projects_page_item():
    return DynamicPageEditMenuItem("page_projects", "مشاريعنا الوقفية", ProjectsPage, "folder-open-inverse", 40)

@hooks.register("register_pages_edit_menu_item")
def register_team_page_item():
    return DynamicPageEditMenuItem("page_team", "فريقنا وخبرائنا", TeamPage, "group", 50)

@hooks.register("register_pages_edit_menu_item")
def register_testimonials_page_item():
    return DynamicPageEditMenuItem("page_testimonials", "قالوا عنا", TestimonialsPage, "openquote", 60)

@hooks.register("register_pages_edit_menu_item")
def register_videos_page_item():
    return DynamicPageEditMenuItem("page_videos", "ألبوم الفيديو", VideosPage, "media", 70)

@hooks.register("register_pages_edit_menu_item")
def register_careers_page_item():
    return DynamicPageEditMenuItem("page_careers", "التوظيف والكفاءات", CareersPage, "user", 75)

@hooks.register("register_pages_edit_menu_item")
def register_contact_page_item():
    return DynamicPageEditMenuItem("page_contact", "تواصل معنا", ContactPage, "mail", 80)


# ==============================================================================
# 3. DIRECT ACCESS TO NAVBAR & HEADER SETTINGS IN ADMIN SIDEBAR
# ==============================================================================

class NavbarSettingsMenuItem(MenuItem):
    def __init__(self):
        self._url = "#"
        super().__init__(
            "القائمة العلوية والنافبار",
            "#",
            name="navbar_settings",
            icon_name="site",
            order=115,
        )

    @property
    def url(self):
        obj = NavbarSettings.get_settings()
        return reverse("wagtailsnippets_home_navbarsettings:edit", args=[obj.id])

    @url.setter
    def url(self, value):
        self._url = value



@hooks.register("register_admin_menu_item")
def register_navbar_settings_menu():
    return NavbarSettingsMenuItem()

