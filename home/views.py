from django.shortcuts import render

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
    return render(request, "home/projects_page.html")

def team_view(request):
    """
    Dedicated 'Our Team' (فريقنا) page for Rafed Endowment Society.
    """
    return render(request, "home/team_page.html")

def testimonials_view(request):
    """
    Dedicated 'Testimonials' (قالوا عنا) page for Rafed Endowment Society.
    """
    return render(request, "home/testimonials_page.html")

def contact_view(request):
    """
    Dedicated 'Contact Us' (تواصل معنا) page for Rafed Endowment Society.
    """
    context = {}
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        context["submitted"] = True
        context["sender_name"] = name or "الكريم"
    return render(request, "home/contact_page.html", context)

