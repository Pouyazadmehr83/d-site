from django.shortcuts import render
from website.models import Contact
from website.forms import ContactFrom, NewsletterForm
from django.http import HttpResponseRedirect

def index_views(request):
    return render(request, "website/index.html")

def about_views(request):
    return render(request, "website/about.html")

def contact_views(request):
    if request.method == 'POST':
        form = ContactFrom(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/contact')  # اضافه کردن redirect
    else:
        form = ContactFrom()

    return render(request, "website/contact.html", {'form': form})

def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return HttpResponseRedirect('/')  # حذف else غیرضروری