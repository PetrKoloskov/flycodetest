from django.shortcuts import render

from .models import Post
def index(request):
    posts=Post.objects.all().count()
    return render(
        request,
        'index.html',
        context={'posts':posts}
    )
# Create your views here.
