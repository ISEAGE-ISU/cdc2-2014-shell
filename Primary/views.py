from django.shortcuts import render
from Primary.models import Post

# Create your views here.

def blog(request):
    blog_data = Post.objects.all()[:5]
    context = { 'blog_data' : blog_data }
    return render(request, 'Primary/index.html', context)