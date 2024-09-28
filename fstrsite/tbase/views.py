from django.shortcuts import render
from rest_framework import generics
from .models import PointAdd
from .serializers import PointAddSerializer


class PointAddAPIView(generics.ListAPIView):
    queryset = PointAdd.objects.all()
    serializer_class = PointAddSerializer
# Create your views here.
