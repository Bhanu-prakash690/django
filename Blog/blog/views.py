from django.shortcuts import render, reverse, HttpResponseRedirect
from .models import Post
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
@login_required(login_url='/accounts/login')
def home(request):
    try:
        posts = request.user.posts.all()
    except:
        posts = []

    return render(request, 'blog/home.html', {'posts':posts})


@login_required(login_url='/accounts/login')
def other_posts(request):
    try:
        posts_ = [post for post in Post.objects.all() if post.user.username != request.user.username and post.mode == False]
    except:
        posts_ = []

    return render(request, 'blog/posts.html', {'posts':posts_})

class create_post(LoginRequiredMixin,View):
    login_url = '/accounts/login'
    def get(self, request):
        return render(request, 'blog/create.html')

    def post(self, request):
        image = request.FILES['image']
        description = request.POST['description']
        try:
            mode = bool(request.POST['mode'])
        except:
            mode = False
        self.request.user.posts.create(image=image, description=description, mode=mode)
        self.request.user.save()
        return HttpResponseRedirect(reverse('home'))
