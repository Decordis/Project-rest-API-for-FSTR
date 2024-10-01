from django.shortcuts import render
from rest_framework import viewsets
from .models import PointAdd, Image, Users, Coord, LevelPoint
from .serializers import PointAddSerializer, ImageSerializer, UsersSerializer, CoordSerializer, LevelPointSerializer


class PointAddAPIView(viewsets.ModelViewSet):
    queryset = PointAdd.objects.all()
    serializer_class = PointAddSerializer


class ImageAPIView(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class UsersAPIView(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class CoordAPIView(viewsets.ModelViewSet):
    queryset = Coord.objects.all()
    serializer_class = CoordSerializer


class LevelAPIView(viewsets.ModelViewSet):
    queryset = LevelPoint.objects.all()
    serializer_class = LevelPointSerializer
