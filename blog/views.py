from django.shortcuts import render,get_object_or_404
from blog.models import Post,category
# Create your views here.
def blog_view(request):
    posts=Post.objects.filter(status = 1)
    context = {'posts':posts}
    return render(request, "blog/blog-home.html",context)

def blog_single(request,pid):
    posts=Post.objects.filter(status = 1)
    posts=get_object_or_404(Post,pk=pid)
    context = {'posts':posts}
    return render(request, "blog/blog-single.html",context)

def test(request):
    posts = Post.objects.filter(status=1)  # یا Post.objects.all()
    context = {'posts': posts}
    return render(request, "test.html", context)

def blog_category(request,cat_name):
     posts=Post.objects.filter(status=1)
     posts=posts.filter(category__name=cat_name)
     context={'posts':posts}
     return render(request,'blog/blog-home.html',context)