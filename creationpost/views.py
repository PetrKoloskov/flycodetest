from django.shortcuts import render
from django.views import generic
from .models import Post
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils import timezone



def index(request):
    posts = Post.objects.all().count()
    return render(
        request,
        'index.html',
        context={'posts': posts}
    )


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

'''
def edit(request, id):
    post=Post.objects.get(id=id)
    try:
        if request.method=='POST':
            post.title=request.POST.get('title')
            post.content=request.POST.get('content')
            post.save()
            return HttpResponseRedirect('/')
        else:
'''


class PostListView(generic.ListView):
    model = Post


class PostDetailView(generic.DetailView):
    model = Post

# Create your views here.
