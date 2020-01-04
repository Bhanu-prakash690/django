from django.urls import path
from .views import *

urlpatterns = [
    path('', upload, name='upload'),
    path('map', map, name='map'),
    path('update_data_base', update_data_base, name='update_data_base'),
    path('data', get_data, name='data'),
    path('detail/<int:pk>', detail, name='detail'),
]
