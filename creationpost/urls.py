from django.urls import path

from flycodetest import settings
from . import views
from django.conf.urls import url
from django.conf.urls.static import static
from .views import TagIndexView
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^posts/$', views.PostListView.as_view(), name='posts'),
    url(r'^post/(?P<pk>\d+)$',views.PostDetailView.as_view(), name='post-detail'),
    url(r'^tag/(?P<slug>[-\w+])/$', TagIndexView.as_view(), name='tagged')

]
urlpatterns += [

    url(r'^post/create/$', views.PostCreate.as_view(), name='post-create'),
    url(r'^post/(?P<pk>\d+)/update/$',views.PostUpdate.as_view(), name='post-update'),
    url(r'^post/(?P<pk>\d+)/delete/$',views.PostDelete.as_view(), name='post-delete'),
]