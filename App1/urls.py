from django.urls import path
from App1.views import *
app_name='App1'
urlpatterns=[
    path('first/',first,name='first'),
]
