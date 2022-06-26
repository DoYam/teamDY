from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Room
from .serializers import RoomSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def room(request):
    if request.method == 'GET':
        totalRoom = Room.objects.all()
        serializer = RoomSerializer(totalRoom, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH', 'DELETE'])
def room_with_id(request, id):
    if request.method == 'PATCH':
        room = get_object_or_404(Room, id=id)
        serializer = RoomSerializer(room, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        room = get_object_or_404(Room, id=id)
        room.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
