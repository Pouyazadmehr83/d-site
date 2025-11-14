from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse
 
def index_views(request):
    return render(request, "website/index.html")

def about_views(request):
    return render(request, "website/about.html")
 
def contact_views(request):
    return render(request, "website/contact.html")

'''def test(request):
    return render(request,"test.html")'''