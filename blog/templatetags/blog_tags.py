
import datetime
from blog.models import category
from django import template
from blog.models import Post

register = template.Library()


@register.simple_tag(name='sum')
def fun():
    posts=Post.objects.filter(status=1).count()
    return posts
@register.inclusion_tag('blog/blog-popular-posts.html')
def latesposts():
    posts=Post.objects.filter(status=1).order_by('published_date')
    return {'posts':posts}

@register.inclusion_tag('blog/blog-catgory.html')
def postcategories():
    posts=Post.objects.filter(status=1)
    categories=category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name.name] = posts.filter(category=name).count()
    return {'categories':cat_dict}