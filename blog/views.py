from django.shortcuts import render
from django.views import generic
from .models import Post


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


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6