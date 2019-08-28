from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post
from django.utils import timezone

# Create your views here.

def home(request):
    posts = Post.objects
    return render(request, 'posts/home.html', {'posts':posts} )

@login_required
def post(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and  request.POST['url']  and request.FILES['image']:
            post = Post()
            post.title = request.POST['title']
            post.body = request.POST['body']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                post.url = request.POST['url']
            else:
                post.url ='http://' + request.POST['url']
            post.image = request.FILES['image']
            post.pub_date = timezone.datetime.now()
            post.hunter = request.user
            post.save()
            return redirect('/posts/' + str(post.id))
        else:
            return render(request, 'posts/post.html', {'error':'All fields are required'})
    else:
        return render(request, 'posts/post.html') 

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'posts/detail.html', {'post': post})