from django.shortcuts import render,get_object_or_404
from blog.models import Post,category,Comment
from blog.forms import CommentForm
from django.contrib import messages
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.
def blog_view(request,**kwargs):
    posts=Post.objects.filter(status=1).order_by('-published_date')  # اضافه کردن order_by
    if kwargs.get("cat_name") !=None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get("author_username") !=None:
        posts = posts.filter(author__username = kwargs['author_username'])
    if kwargs.get("tag_name") !=None:
        posts = posts.filter(tags__name__in=[kwargs['tag_name']])

    paginator = Paginator(posts,3)  # تغییر نام به paginator
    try:
        page_number = request.GET.get('page')
        posts = paginator.get_page(page_number)  # استفاده از paginator.get_page
    except PageNotAnInteger:
        posts = paginator.get_page(1)
    except EmptyPage:
        posts = paginator.get_page(1)
            
    context = {'posts':posts}
    return render(request, "blog/blog-home.html",context)

def blog_single(request, pid):
    post = get_object_or_404(Post, pk=pid)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post     # ست کردن پست
            comment.save()
            messages.success(request, 'Your comment has been submitted successfully.')
        else:
            messages.error(request, 'There was an error submitting your comment.')
    else:
        form = CommentForm()

    comments = Comment.objects.filter(post=post, approved=True).order_by('-created_date')

    context = {
        'posts': post,
        'comments': comments,
        'form': form,
    }
    return render(request, "blog/blog-single.html", context)


def test(request):
    posts = Post.objects.filter(status=1)  # یا Post.objects.all()
    context = {'posts': posts}
    return render(request, "test.html", context)

def blog_category(request,cat_name):
     posts=Post.objects.filter(status=1)
     posts=posts.filter(category__name=cat_name)
     context={'posts':posts}
     return render(request,'blog/blog-home.html',context)

def search_blog(request):
    posts=Post.objects.filter(status=1)
    if request.method == 'GET' :
        if s:=request.GET.get('s'):
            posts = posts.filter(content__contains=s)
    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)