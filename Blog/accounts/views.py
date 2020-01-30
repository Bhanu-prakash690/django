from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
#from .models import Profile
from django.contrib import messages
import random
# Create your views here.

def signup(request):
    if request.method == 'GET':
        a = request.session['a'] = random.randrange(1,10)
        b = request.session['b'] = random.randrange(1,10)
        return render(request, 'accounts/signup.html', {'a':a, 'b':b})
    else:
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        try:
            u = User.objects.get(username=username)
        except:
            u = None
        if u:
            messages.error(request, f'User {u.username} already exist')
            return HttpResponseRedirect(reverse('signup'))
        else:
            if password1 == password2:
                a = request.session['a']
                b = request.session['b']
                print((a,b))
                if int(request.POST['captca']) == a+b:
                    user = User.objects.create_user(username, email, password1)
                    user.save()
                    return HttpResponseRedirect(reverse('login'))
                else:
                    messages.warning(request, 'enter correct captca')
                    return HttpResponseRedirect(reverse('signup'))
            else:
                messages.warning(request, 'enter correct password')
                return HttpResponseRedirect(reverse('signup'))

def login_user(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
        else:
            messages.warning(request, 'error trying to login')
            return HttpResponseRedirect(reverse('login'))
    else:
        return render(request, 'accounts/login.html')

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
