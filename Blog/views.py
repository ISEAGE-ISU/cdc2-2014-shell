from django.shortcuts import render
from Blog.models import Post

# Create your views here.

def Post_View(request):
    post_data = Post.objects.all()[:5]
    context = { 'post_data' : post_data }
    return render(request, 'Blog/index.html', context)