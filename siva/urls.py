from django.urls import path

from siva.views import *

app_name = 'Siva'

urlpatterns = [
    path('si/',si,name='si'),
]