from django.shortcuts import render

def about_view(request):
    """
    Dedicated 'About Us' (من نحن) page for Rafed Endowment Society.
    """
    return render(request, "home/about_page.html")
