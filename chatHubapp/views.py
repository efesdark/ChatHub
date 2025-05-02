from django.shortcuts import render

# Create your views here.
# chathubapp/views.py
from django.http import HttpResponse

def test(request):
    return HttpResponse("Merhaba, ChatHub'a hoş geldiniz!")

def home(request):
    return render(request, 'chatHubapp/home.html')
