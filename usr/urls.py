from django.conf.urls import include, url
from usr.views import *

urlpatterns =[
    url(r'^search/', search),
    url(r'^index/', index)
]