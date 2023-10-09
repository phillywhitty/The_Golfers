from django.shortcuts import render
from django.http import HttpResponse

def landing_page(request):
    """
    Render the landing_page.html template
    """
    return render(request, "landing_page.html")

def about(request):
    """
    Render the about.html template
    """
    return render(request, "about.html")



def index(request):
    """
    Render the index.html template
    """
    return render(request, "index.html")




