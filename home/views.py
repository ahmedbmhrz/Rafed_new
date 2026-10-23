from django.shortcuts import render
from .models import VideoItem, ProjectItem, TeamMember, TestimonialItem, ContactInquiry, SiteContactSettings

def about_view(request):
    """
    Dedicated 'About Us' (من نحن) page for Rafed Endowment Society.
    """
    return render(request, "home/about_page.html")

def services_view(request):
    """
    Dedicated 'Our Services' (خدماتنا) page for Rafed Endowment Society.
    """
    return render(request, "home/services_page.html")

def projects_view(request):
    """
    Dedicated 'Our Projects' (مشاريعنا) page for Rafed Endowment Society.
    """
    projects = ProjectItem.objects.filter(is_featured=True)
    return render(request, "home/projects_page.html", {"projects": projects})

def team_view(request):
    """
    Dedicated 'Our Team' (فريقنا) page for Rafed Endowment Society.
    """
    team_members = TeamMember.objects.filter(is_active=True)
    return render(request, "home/team_page.html", {"team_members": team_members})

def testimonials_view(request):
    """
    Dedicated 'Testimonials' (قالوا عنا) page for Rafed Endowment Society.
    """
    testimonials = TestimonialItem.objects.filter(is_featured=True)
    return render(request, "home/testimonials_page.html", {"testimonials": testimonials})

def contact_view(request):
    """
    Dedicated 'Contact Us' (تواصل معنا) page for Rafed Endowment Society.
    Saves incoming inquiries into ContactInquiry model for admin review.
    """
    context = {}
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

def videos_view(request):
    """
    Dedicated 'Video Album' (ألبوم الفيديو) page for Rafed Endowment Society.
    """
    videos = VideoItem.objects.filter(is_active=True)
    return render(request, "home/videos_page.html", {"videos": videos})

