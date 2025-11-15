 
from django.urls import path
from website.views  import *

app_name = 'website'

urlpatterns = [
    path("",index_views,name='index'),
    path("about",about_views,name='about'),
    path("contact",contact_views,name='contact'),
    path("newsletter",newsletter_view,name='newsletter'),
    #path("test",test,name='test')
]
