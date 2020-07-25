from django.urls import path
from . import views
import re
from django.conf.urls import url
urlpatterns = [
    path('', views.index,name='index'),
    path(r'^posts/$', views.PostListView.as_view(),name='posts')
]