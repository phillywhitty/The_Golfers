from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from . forms import CreateBlogForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from . models import GolfCourse



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

@login_required(login_url="account/login.html")
def blog_index(request):

    return render(request, "blog_index.html")



# ==============================
# CRUD VIEWS
# ==============================


# Render the CREATE blog page
@login_required(login_url="account/login.html")
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

# Lets a user READ a blog they created on my_golf_blog page
@login_required(login_url="account/login.html")
def my_golf_blog(request):

    current_user = request.user.id

    my_blog = GolfCourse.objects.all().filter(user=current_user)

    context = {'MyBlog': my_blog}



    return render(request, "my_golf_blog.html", context)

# Lets a user UPDATE a blog on my_golf_blog page
@login_required(login_url="account/login.html")
def update_blog(request, pk):

    try:

        update = GolfCourse.objects.get(id=pk, user=request.user)

    except:

        return redirect('my_golf_blog')

    form = CreateBlogForm(instance=update)

    if request.method == 'POST':

        form = CreateBlogForm(request.POST, instance=update)

        if form.is_valid():

            form.save()
            messages.success(request, "Your Blog has been updated!")

            return redirect('my_golf_blog')

    context = {'UpdateBlog': form}

    return render(request, "update_blog.html", context)