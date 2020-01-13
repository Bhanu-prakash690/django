from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('find_friends/', find_friends, name="find_friends"),
    path('friend_requests/', friend_requests, name="friend_requests"),
    path('send_request/<str:name>', send_request, name="send_request"),
    path('accept_request/<str:name>', accept_request, name="accept_request"),
    path('chat/<str:room_name>/', chat, name='chat'),
    path('roomNames/', roomName, name="roomNames"),
]
