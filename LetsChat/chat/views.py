from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.models import User
from accounts.models import Friends
from django.http import JsonResponse
from django.views.decorators.clickjacking import xframe_options_exempt
from django.contrib.auth.decorators import login_required
import hashlib
# Create your views here.


@login_required(login_url='/accounts/login')
def index(request):
    users = [user.name for user in request.user.profile.friends_set.all() if user.name != request.user.username]
    roomNames = [( User.objects.get(username=user2), hashlib.md5("".join(list(sorted((request.user.username, user2)))).encode()).hexdigest() ) for user2 in users]
    print(roomNames)
    context = {
        "room_names":roomNames
    }
    return render(request, 'index.html', context)

@login_required(login_url='/accounts/login')
def find_friends(request):
    users = [user for user in User.objects.all() if user.username!="rohit" and user.username!=request.user.username and (user.username not in [x.name for x in request.user.profile.friends_set.all()])]
    context = {
        "users":users
    }
    return render(request, 'findFriends.html', context)

@login_required(login_url='/accounts/login')
def friend_requests(request):
    friends = [(friend.name, User.objects.get(username=friend.name).profile.image.url) for friend in Friends.objects.all() if friend.friend.user.username==request.user.username and friend.accepted == False]
    context = {
        "friends":friends
    }
    return render(request, 'friendRequests.html', context)

@login_required(login_url='/accounts/login')
def send_request(request, name):
    friends1 = Friends(friend=request.user.profile,name=name, accepted=True)
    friends1.save()
    user = User.objects.get(username=name)
    friends2 = Friends(friend=user.profile, name=request.user.username)
    friends2.save()
    return HttpResponseRedirect(reverse('friend_requests'))

@login_required(login_url='/accounts/login')
def accept_request(request, name):
    friend = request.user.profile.friends_set.get(name=name)
    friend.accepted = True
    friend.save()
    return HttpResponseRedirect(reverse('friend_requests'))


@login_required(login_url='/accounts/login')
def roomName(request):
    users = [user.name for user in request.user.profile.friends_set.all() if user.name != request.user.username]
    roomNames = ["".join(list(sorted((request.user.username, user2)))) for user2 in users]
    json_ = {
        "roomNames":roomNames
    }
    return JsonResponse(json_)

@login_required(login_url='/accounts/login')
@xframe_options_exempt
def chat(request, room_name):
    context = {
        "room":room_name
    }
    return render(request, 'chat.html', context)
