from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from . forms import CreateBlogForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages




# ==============================
# View functions
# ==============================

# Render the landing_page

def landing_page(request):

    return render(request, "landing_page.html")

# Render the about page

def about(request):

    return render(request, "about.html")

# Render the blog_index page

@login_required
def blog_index(request):

    return render(request, "blog_index.html")

# Render the ballybunnion page

def ballybunnion_blog(request):

    return render(request, "ballybunnion_blog.html")

# Render the doonbeg page

def doonbeg_blog(request):

    return render(request, "doonbeg_blog.html")

# Render the k club page

def k_club_blog(request):

    return render(request, "k_club_blog.html")



# Render the create blog page

def create_blog(request):
    form = CreateBlogForm
    # Check if the request method is POST
    if request.method == 'POST':
        form = CreateBlogForm(request.POST)
    # Check if the form data is valid
        if form.is_valid():
            createblog = form.save(commit=False)
            createblog.user = request.user
            createblog.save()
            messages.success(request, "Your Blog has been submitted!")
            return redirect('blog_index')
    context = {'CreateBlogForm': form}

    return render(request, "create_blog.html", context)






