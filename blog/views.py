from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import GolfCourse, Comment
from .forms import CommentForm



# ==============================
# View functions
# ==============================
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

def ballybunnion_blog(request):
    """
    Render the ballybunnion.html template
    """
    return render(request, "ballybunnion_blog.html")

def doonbeg_blog(request):
    """
    Render the doonbeg.html template
    """
    return render(request, "doonbeg_blog.html")

def k_club_blog(request):
    """
    Render the k_club.html template
    """
    return render(request, "k_club_blog.html")


# views.py



def golf_course_detail(request, pk):
    golf_course = GolfCourse.objects.get(default=None)(pk=pk)
    comments = golf_course.comments.filter(approved=True)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.golf_course = golf_course
            comment.save()
            return redirect('golf_course_detail', pk=pk)
    else:
        form = CommentForm()
    return render(request, 'golf_course_detail.html', {'golf_course': golf_course, 'comments': comments, 'form': form})

