from django.shortcuts import render
from rest_framework import generics

from cafeterias.models import Cafeteria
from cafeterias.serializers import CafeteriaSerializer


class CafeView(generics.ListAPIView):
	serializer_class = CafeteriaSerializer
	queryset = Cafeteria.objects.all()
