from django.shortcuts import render, redirect#redirect added
from .forms import RegisterForm  #import RegisterForm class from created forms.py for user registeration
from django.contrib import messages
from django.contrib.auth import authenticate,login# for profilising authenticate and loginn added
from django.contrib.auth.decorators import login_required#added for profile section login control 
from django.contrib.auth import logout#added for logout feature
# Create your views here.
# chathubapp/views.py



#for connecting to chatbot

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
#from openai import OpenAI
from django.conf import settings
import json
import os
#import requests
#client = OpenAI(api_key=settings.OPENAI_API_KEY)

import requests

HUGGINGFACE_API_KEY= os.getenv("HUGGINGFACE_API_KEY")
from .models import ChatMessage

from django.http import HttpResponse



def test(request):
    return HttpResponse("Welcome to ChatHub!")

def home(request):
    return render(request, 'chatHubapp/home.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profile')  # başarılıysa profil sayfasına yönlendir
        else:
            messages.error(request, 'Kullanıcı adı veya şifre hatalı.')

    return render(request, 'chatHubapp/login.html')

def user_logout(request):#added for logout feature
    logout(request)
    return redirect('login')


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

@login_required#for this function login_required decarator
def profile(request):

    return render(request, 'chatHubapp/profile.html', {'user': request.user})
#print(HUGGINGFACE_API_KEY)
print("HUGGINGFACE_API_KEY exists:", bool(os.getenv("HUGGINGFACE_API_KEY")))

def chat_view(request):
    return render(request, 'chatHubapp/chat.html')

from .chatbot import generate_response

@csrf_exempt  # Geliştirme ortamında CSRF'yi devre dışı bırak (geçici)
def chat_api(request):
    if request.method == "POST":
        try:
            user_message = request.POST.get("message", "")
            bot_response = generate_response(user_message)
            return JsonResponse({"response": bot_response})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    return JsonResponse({"error": "Sadece POST istekleri desteklenir."}, status=405)
