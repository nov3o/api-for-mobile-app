from django.db.models import Q
from rest_framework import generics
from datetime import datetime

from cafeterias.models import Cafeteria
from schedules.models import Schedule

from api.serializers import MenuSerializer
from food.serializers import FoodItemSerializer
from schedules.serializers import ScheduleSerializer
from categories.serializers import CategorySerializer
from cafeterias.serializers import CafeteriaSerializer


class TodayMenu(generics.ListAPIView):
	serializer_class = MenuSerializer

	def get_queryset(self):
		return Schedule.objects.filter(
			Q(week_day=datetime.today().weekday()),
			Q(cafe_id=self.kwargs['cafe_id'])
			)

	def get_serializer_context(self):
		return {
			'date': datetime.today().weekday(),
			'time': datetime.now()
			}


class OneDayMenu(generics.ListAPIView):
	serializer_class = MenuSerializer

	def get_queryset(self):
		return Schedule.objects.filter(
			Q(week_day=self.kwargs['wd']),
			Q(cafe_id=self.kwargs['cafe_id'])
			)

	def get_serializer_context(self):
		return {
			'date': datetime.today().weekday(),
			'time': None
			}
