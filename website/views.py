from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse
import requests

def index_views(request):
    return HttpResponse("<h1>home page</h1>")

def about_views(request):
    return HttpResponse("<h1>about page</h1>")
 
def contact_views(request):
    return HttpResponse("<h1><contact page/h1>")
