from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
# Create your views here. 

# def home(request):
#     return HttpResponse("Hello world!")
posts=[
    {
    "author":"syedamuskan811@gmail.com",
    "name"    :"muskan",
    "phone" : "987654321"

    }
]

def index(request):
    context= {
        'posts':posts

    }
    return render(request, 'index.html',context)

def about(request):
     context= {
        'posts':posts

    }
     return render(request, 'about.html',context)


def contact(request):
     context= {
        'posts':posts

    }
     return render(request, 'register.html',context)
