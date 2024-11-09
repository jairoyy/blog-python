from django.shortcuts import render , redirect
from django.http import HttpResponse

# Create your views here. 

def index(request):
    return HttpResponse("Hi ,This is my First Blog page")

def detail(request):
    return HttpResponse("This  is My Blog Details page and Details are shown here")


def about(request):
    return HttpResponse("This is my About page and here you can see about me in this page")

def old_url_redirect(request):
    return redirect("new_url")


def new_url_view(request):
    return HttpResponse("This is new urls.")