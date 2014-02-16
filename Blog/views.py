from django.shortcuts import render
from django.http import Http404
from Blog.models import Post

# Create your views here.

def frontpage(request):
    post_data = Post.objects.all().order_by('-date')
    context = { 'post_data' : post_data , 'NAV4' : True}
    return render(request, 'Blog/blog.html', context)

def single_post(request, post_id):
    try:
        post_data = Post.objects.get(pk=post_id)
        #post_data = Post.objects.all().order_by('-date')[:5]

    except Post.DoesNotExist:
        raise Http404
    context = {'post_data' : post_data}
    return render(request, 'Blog/post.html', context)