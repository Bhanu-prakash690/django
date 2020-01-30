from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('create', create_post.as_view(), name='create_post'),
    path('posts', other_posts, name='posts'),
]
