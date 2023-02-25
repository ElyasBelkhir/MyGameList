from asyncio import as_completed
from django.urls import path
from .views import list
from . import views
from rest_framework import routers


urlpatterns = [

    path('', list, name="index")
   
]