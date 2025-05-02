from django.shortcuts import render

# Create your views here.
# chathubapp/views.py
from django.http import HttpResponse

def home(request):
    return HttpResponse("Merhaba, ChatHub'a hoş geldiniz!")