from django.shortcuts import render, redirect#redirect added
from .forms import RegisterForm  #import RegisterForm class from created forms.py for user registeration
from django.contrib import messages
# Create your views here.
# chathubapp/views.py
from django.http import HttpResponse

def test(request):
    return HttpResponse("Welcome to ChatHub!")

def home(request):
    return render(request, 'chatHubapp/home.html')

def login(request):
    return render(request, 'chatHubapp/login.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created, you can login now')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'chatHubapp/register.html', {'form': form})

def profile(request):
    return render(request, 'chatHubapp/profile.html')