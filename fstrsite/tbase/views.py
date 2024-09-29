from django.shortcuts import render
from rest_framework import generics
from .models import PointAdd, Image, Users
from .serializers import PointAddSerializer, ImageSerializer, UsersSerializer


class PointAddAPIView(generics.ListAPIView):
    queryset = PointAdd.objects.all()
    serializer_class = PointAddSerializer


class ImageAPIView(generics.ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class UsersAPIView(generics.ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
