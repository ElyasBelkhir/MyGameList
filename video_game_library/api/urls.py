from asyncio import as_completed
from django.urls import path
from .views import roomViewSet, gameCreate, gameUpdate, gameDelete, gameList, gameDetail
from rest_framework import routers


urlpatterns = [

    path('', roomViewSet.as_view()),
    path('game-list', gameList, name='game-list'),
    path('game-list/<str:pk>', gameDetail, name='game-list'),
    path('game-create', gameCreate, name='game-create'),
    path('game-create/<str:pk>', gameUpdate, name='game-create'),
    path('game-delete/<str:pk>', gameDelete, name='game-delete'),


]