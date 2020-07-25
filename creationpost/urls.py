from django.urls import path
from . import views
from django.conf.urls import url
urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^posts/$', views.PostListView.as_view(),name='posts'),
    url(r'^post/(?P<pk>\d+)$',views.PostDetailView.as_view(),name='post-detail')

]