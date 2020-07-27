from django.shortcuts import render
from django.views import generic
from .models import Post
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils import timezone


def index(request):
    return render(
        request,
        'index.html'
    )

class TagIndexView(generic.ListView):
    template_name = 'creationpost/post_list.html'
    model = Post
    context_object_name = 'post_list'
    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs.get('slug'))


class PostCreate(CreateView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('posts')

class PostUpdate(UpdateView):
    model = Post
    fields = ['title', 'content', 'image','tags']
    model.pub_date = timezone.now()
    success_url = reverse_lazy('posts')

class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('posts')

class PostListView(generic.ListView):
    model = Post

class PostDetailView(generic.DetailView):
    model = Post

# Create your views here.
