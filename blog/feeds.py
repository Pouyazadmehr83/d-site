from django.contrib.syndication.views import Feed
from django.urls import reverse
from blog.models import Post

class LatestPostsFeed(Feed):
    title = "My Blog RSS Feed"
    link = "/rss/"
    description = "Latest posts from my blog."

    def items(self):
        return Post.objects.filter(status=1).order_by('-created_date')[:10]  # یا هر شرط دیگری

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content  # اگر خلاصه داری می‌تونی خلاصه را بذاری

    def item_link(self, item):
        return reverse('blog:single', args=[item.id])
