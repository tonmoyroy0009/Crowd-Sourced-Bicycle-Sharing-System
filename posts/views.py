from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from django.utils import timezone

# Create your views here.

def home(request):
    return render(request, 'posts/home.html')

@login_required
def post(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and  request.POST['url'] and request.FILES['icon'] and request.FILES['image']:
            post = Post()
            post.title = request.POST['title']
            post.body = request.POST['body']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                post.url = request.POST['url']
            else:
                post.url ='http://' + request.POST['url']
            post.icon = request.FILES['icon']
            post.image = request.FILES['image']
            post.pub_date = timezone.datetime.now()
            post.votes_total = 1
            post.hunter = request.user
            post.save()
            return redirect('home')
        else:
            return render(request, 'posts/post.html', {'error':'All fields are required'})
    else:
        return render(request, 'posts/post.html') 