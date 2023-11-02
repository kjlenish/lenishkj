from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from django.contrib.auth import login, authenticate
from django.contrib import messages
from users.forms import LoginForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def base(request):
    if not request.user.is_authenticated:  # Check if the user is not authenticated
        form = LoginForm(request.POST)
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, f"Logged in as {username}!")
                    return redirect('blog-home')
                else:
                    messages.warning(request, 'Wrong Username or password')

        context = {'form': form}
        return render(request, 'base/home.html', context)

    return render(request, 'base/home.html')

@login_required
def home(request):              
    context = {'posts': Post.objects.all()}
    return render(request, 'blog\home.html', context)