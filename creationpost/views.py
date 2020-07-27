from django.shortcuts import render
from django.views import generic
from .models import Post
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils import timezone

from taggit.models import Tag


def index(request):
    posts = Post.objects.all().count()
    return render(
        request,
        'index.html',
        context={'posts': posts}
    )


class TagIndexView(generic.ListView):
    template_name = 'creationpost/post_list.html'
    model = Post
    paginate_by = '10'
    context_object_name = 'posts'
    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs.get('slug'))


class PostCreate(CreateView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('posts')

class PostUpdate(UpdateView):
    model = Post
    fields = ['title', 'content', 'image']
    model.pub_date=timezone.now()
    success_url = reverse_lazy('posts')

class PostDelete(DeleteView):

    model = Post
    success_url = reverse_lazy('posts')



class PostListView(generic.ListView):
    model = Post


class PostDetailView(generic.DetailView):
    model = Post

# Create your views here.
