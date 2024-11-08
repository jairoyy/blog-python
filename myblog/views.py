from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Hello, This is my first blog")

def detail(request ,post_id):
    return HttpResponse(f"You are viewing blog detail page and ID is {post_id} ")