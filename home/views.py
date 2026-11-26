from django.shortcuts import render
from .models import (
    HomePage, AboutPage, ServicesPage, ProjectsPage, TeamPage, TestimonialsPage, VideosPage, ContactPage,
    CareersPage, ContactInquiry, SiteContactSettings
)

def about_view(request):
    """
    Dedicated 'About Us' (من نحن) page for Rafed Endowment Society.
    Loads dynamic story, values, goals, and stats from AboutPage model.
    """
    page = AboutPage.objects.first()
    values = page.values.filter(is_active=True) if page else []
    goals = page.goals.filter(is_active=True) if page else []
    stats = page.stats.filter(is_active=True) if page else []
    return render(request, "home/about_page.html", {
        "page": page,
        "values": values,
        "goals": goals,
        "stats": stats,
    })

def services_view(request):
    """
    Dedicated 'Our Services' (خدماتنا) page for Rafed Endowment Society.
    Loads dynamic services catalog, process steps, and differentiators from ServicesPage model.
    """
    page = ServicesPage.objects.first()
    services = page.services.filter(is_active=True) if page else []
    process_steps = page.process_steps.filter(is_active=True) if page else []
    differentiators = page.differentiators.filter(is_active=True) if page else []
    return render(request, "home/services_page.html", {
        "page": page,
        "services": services,
        "process_steps": process_steps,
        "differentiators": differentiators,
    })

def projects_view(request):
    """
    Dedicated 'Our Projects' (مشاريعنا) page. Loads dynamic projects from ProjectsPage.
    """
    page = ProjectsPage.objects.first()
    projects = page.projects.filter(is_featured=True) if page else []
    return render(request, "home/projects_page.html", {"page": page, "projects": projects})

def team_view(request):
    """
    Dedicated 'Our Team' (فريقنا) page. Loads dynamic members from TeamPage.
    """
    page = TeamPage.objects.first()
    team_members = page.team_members.filter(is_active=True) if page else []
    return render(request, "home/team_page.html", {"page": page, "team_members": team_members})

def testimonials_view(request):
    """
    Dedicated 'Testimonials' (قالوا عنا) page. Loads dynamic testimonials from TestimonialsPage.
    """
    page = TestimonialsPage.objects.first()
    testimonials = page.testimonials.filter(is_featured=True) if page else []
    return render(request, "home/testimonials_page.html", {"page": page, "testimonials": testimonials})

def videos_view(request):
    """
    Dedicated 'Video Album' (ألبوم الفيديو) page. Loads dynamic videos from VideosPage.
    """
    page = VideosPage.objects.first()
    videos = page.videos.filter(is_active=True) if page else []
    return render(request, "home/videos_page.html", {"page": page, "videos": videos})

def contact_view(request):
    """
    Dedicated 'Contact Us' (تواصل معنا) page.
    Saves incoming inquiries into ContactInquiry model for admin review.
    """
    page = ContactPage.objects.first()
    context = {"page": page}
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        phone = request.POST.get("phone", "").strip()
        email = request.POST.get("email", "").strip()
        subject = request.POST.get("subject", "").strip()
        message = request.POST.get("message", "").strip()
        prefer_whatsapp = request.POST.get("prefer_whatsapp") is not None

        if name and phone:
            try:
                ContactInquiry.objects.create(
                    name=name,
                    phone=phone,
                    email=email,
                    subject=subject,
                    message=message,
                    prefer_whatsapp=prefer_whatsapp,
                )
            except Exception as e:
                print("Error saving inquiry:", e)

        context["submitted"] = True
        context["sender_name"] = name or "الكريم"

    return render(request, "home/contact_page.html", context)


def careers_view(request):
    """
    Dedicated 'Careers' (التوظيف والفرص المهنية) page.
    Loads dynamic jobs and benefits from CareersPage model.
    """
    page = CareersPage.objects.first()
    jobs = page.jobs.filter(is_active=True) if page else []
    benefits = page.benefits.filter(is_active=True) if page else []
    return render(request, "home/careers_page.html", {
        "page": page,
        "jobs": jobs,
        "benefits": benefits,
    })

