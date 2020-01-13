from django.urls import path
from .consumer import *

websocket_urlpatterns = [
    path('ws/chat/<str:room_name>/', ChatConsumer),
]
