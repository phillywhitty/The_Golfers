from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic, View
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

def custom_login(request):
    """
    Render the login.html template
    """
    return render(request, "account/login.html")    



def index(request):
    """
    Render the index.html template
    """
    
    return render(request, "index.html", {})


def custom_signup(request):
    """
    Render the signup.html template
    """
    
    return render(request, "account/signup.html", {})


 
class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6
    context_object_name = 'post_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Queryset for The K Club blog posts
        context['k_club_posts'] = Post.objects.filter(status=True, category='The K Club').order_by("-created_on")

        # Queryset for Ballybunnion blog posts
        context['ballybunnion_posts'] = Post.objects.filter(status=True, category='Ballybunnion').order_by("-created_on")

        # Queryset for The Abbey blog posts
        context['the_abbey_posts'] = Post.objects.filter(status=True, category='The Abbey').order_by("-created_on")

        
        return context


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "index.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked
            },
        )
