from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic, View
from .models import Post
from .forms import CommentForm



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

def k_club(request):
    return render(request, 'k_club.html')

def index(request):
    """
    Render the index.html template
    """
    
    return render(request, "index.html", {})


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6
    context_object_name = 'post_list'

class KClubPosts(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "k_club.html"
    paginate_by = 6
    context_object_name = 'k_club_posts'


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
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


from django.contrib.auth.decorators import login_required

@login_required
def post_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        body = request.POST.get('body')
        if body:
            Comment.objects.create(post=post, user=request.user, body=body, approved=True)

    return redirect('post_detail', post_id=post_id)