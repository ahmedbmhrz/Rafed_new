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
