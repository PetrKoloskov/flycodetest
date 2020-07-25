from django.shortcuts import render
from django.views import generic
from .models import Post

def index(request):
    posts=Post.objects.all().count()
    return render(
        request,
        'index.html',
        context={'posts':posts}
    )

class PostListView(generic.ListView):
    model= Post
class PostDetailView(generic.DetailView):
    model = Post
# Create your views here.
