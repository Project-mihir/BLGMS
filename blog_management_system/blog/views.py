# blog/views.py

from django.shortcuts import render, redirect  # Import render and redirect functions
from django.contrib import messages  # Import Django's messaging framework
from .forms import UserRegisterForm  # Import the UserRegisterForm from forms.py
from .models import Post  # Import your Post model

# Define the register view
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)  # Create a form instance with POST data
        if form.is_valid():  # Check if the form is valid
            form.save()  # Save the user to the database
            username = form.cleaned_data.get('username')  # Get the username from the form
            messages.success(request, f'Account created for {username}!')  # Display success message
            return redirect('blog-home')  # Redirect to the home page
    else:
        form = UserRegisterForm()  # Display an empty form if the request is GET
    return render(request, 'blog/register.html', {'form': form})  # Render the registration template with the form

# Define the home view
def home(request):
    posts = Post.objects.all()  # Fetch all posts from the database
    return render(request, 'blog/home.html', {'posts': posts})  # Render the home.html template with the posts
