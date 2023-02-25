from rest_framework import generics, status
from .models import Game
from .serializers import GameSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.renderers import TemplateHTMLRenderer




1# Create your views here.


class roomViewSet(generics.CreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'/task-list',
        'Detail View':'/task-detail/<str:pk>',
        'Create':'/task-create/',
        'Update':'/task-create/<str:pk>',
        'Delete':"/task-delete/<str:pk>/",
    }

    return Response(api_urls)

@api_view(['GET'])
def gameList(request):
    games = Game.objects.all().order_by('-id')
    serializer = GameSerializer(games, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def gameDetail(request, pk):
    games = Game.objects.get(id=pk)
    serializer = GameSerializer(games, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def gameCreate(request):
    serializer = GameSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def gameUpdate(request, pk):
    game = Game.objects.get(id=pk)
    serializer = GameSerializer(instance=game, data=request.data)

    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def gameDelete(request, pk):
    game = Game.objects.get(id=pk)
    game.delete()

    return Response('Item successfully deleted')





