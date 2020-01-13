from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Profile


# Create your views here.

def signup(request):
    if request.method == 'GET':
        return render(request, 'accounts/signup.html')
    else:
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phonenumber']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        photo = request.FILES['photo']
        try:
            u = User.objects.get(username=username)
        except:
            u = None
        if u:
            return HttpResponseRedirect(reverse('signup'))
        else:
            if password1 == password2:
                user = User.objects.create_user(username, email, password1)
                user.save()
                profile = Profile(user=user, phonenumber=phone, image=photo)
                profile.save()
                return HttpResponseRedirect(reverse('login'))
            else:
                return HttpResponseRedirect(reverse('signup'))

def login_user(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return HttpResponseRedirect(reverse('login'))
    else:
        return render(request, 'accounts/login.html')

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
