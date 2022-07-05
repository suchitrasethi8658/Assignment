from django.urls import path
from App2.views import *
app_name='App2'
urlpatterns=[
    path('second/',second,name='second'),
    ]

