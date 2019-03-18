from rest_framework import viewsets

from cafeterias.models import Cafeteria
from api.serializers import CafeteriaSerializer

class CafeView(viewsets.ModelViewSet):
	queryset = Cafeteria.objects.all()
	serializer_class = CafeteriaSerializer
