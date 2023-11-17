from django.urls import path

from sree.views import *

app_name = 'Sreenu'

urlpatterns = [
    path('sr/',sr,name='sr'),
]