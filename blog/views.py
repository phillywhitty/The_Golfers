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
#------------------------
def landing_page(request):
    return render(request, "landing_page.html")


# Render the about page
#----------------------
def about(request):
    return render(request, "about.html")


# Render the blog_index page
#---------------------------
@login_required(login_url="account/login.html")
def blog_index(request):
    return render(request, "blog_index.html")


# ==============================
# CRUD VIEWS
# ==============================

#------------======-----------#
# Render the CREATE blog page #
# -----------======-----------#

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

    # create a context dictionary with the form and pass it to the template
    context = {'CreateBlogForm': form}
    # Render the 'create_blog.html' template with the context data
    return render(request, "create_blog.html", context)


#-------------====-----------------------------------------#
# Lets a user READ a blog they created on my_golf_blog page
#-------------====-----------------------------------------#

@login_required(login_url="account/login.html")
def my_golf_blog(request):
    # Get the ID of the current user
    current_user = request.user.id
    # Retrieve all GolfCourse objects where the user is the current user
    my_blog = GolfCourse.objects.all().filter(user=current_user)
    context = {'MyBlog': my_blog}
    # Render the my_golf_blog.html template with the context data
    return render(request, "my_golf_blog.html", context)


#-------------======----------------------------#
# Lets a user UPDATE a blog on my_golf_blog page
#-------------======----------------------------#
@login_required(login_url="account/login.html")
def update_blog(request, pk):
    # Attempt to retrieve the blog with the given id and owned by the current user
    try:
        blog = GolfCourse.objects.get(id=pk, user=request.user)
    except:
    # If the blog does not exist or does not belong to the current user, redirect to my_golf_blog page
        return redirect('my_golf_blog')

    # Create a form instance with the blog data to be updated
    form = CreateBlogForm(instance=blog)
    
    # Check if the submitted form data is valid
    if request.method == 'POST':
        form = CreateBlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, "Your Blog has been updated!")
            return redirect('my_golf_blog')
    context = {'UpdateBlog': form}
    # Render the update_blog.html template with the context data
    return render(request, "update_blog.html", context)


#-------------======----------------------------#
# Lets a user DELETE a blog on my_golf_blog page
#-------------======----------------------------#
@login_required(login_url="account/login.html")
def delete_blog(request, pk):
    # Attempt to retrieve the blog with the given id and owned by the current user
    try :
        blog = GolfCourse.objects.get(id=pk, user=request.user)
    # If the blog does not exist or does not belong to the current user, redirect to my_golf_blog page
    except:
        return redirect('my_golf_blog')
    # Check if the submitted form data is valid
    if request.method == 'POST':
        blog.delete()
        messages.success(request, "Your Blog has been deleted!")
        return redirect('my_golf_blog')

    # Render the delete_blog.html template with the context data
    return render(request, "delete_blog.html")