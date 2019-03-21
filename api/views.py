from django.db.models import Q
from rest_framework import generics
from datetime import datetime

from cafeterias.models import Cafeteria
from schedules.models import Schedule
from api.serializers import (CafeteriaSerializer,
	MenuSerializer, ScheduleSerializer)


class CafeView(generics.ListAPIView):
	serializer_class = CafeteriaSerializer
	queryset = Cafeteria.objects.all()


class DaySchedule(generics.ListAPIView):
	serializer_class = ScheduleSerializer

	def get_queryset(self):
		cid = self.kwargs['cafe_id']
		wd = datetime.today().weekday()
		return Schedule.objects.filter(Q(week_day=wd)).filter(Q(cafe_id=cid))


class TodaySchedule(generics.ListAPIView):
	serializer_class = ScheduleSerializer
	queryset = Schedule.objects.all()


class OneDaySchedule(generics.ListAPIView):
	serializer_class = ScheduleSerializer

	def get_queryset(self):
		wd = self.kwargs['wd']
		cid = self.kwargs['cafe_id']
		return Schedule.objects.filter(Q(week_day=wd), Q(cafe_id=cid))


class AllCafes(generics.ListAPIView):
	serializer_class = ScheduleSerializer

	def get_queryset(self):
		wd = self.kwargs['wd']
		return Schedule.objects.filter(Q(week_day=wd))


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
	serializer_class = MenuSerializer(context={
		'date': datetime.today().weekday(),
		'time': None
		})

	def get_queryset(self):
		return Schedule.objects.filter(
			Q(week_day=self.kwargs['wd']),
			Q(cafe_id=self.kwargs['cafe_id'])
			)

	def get_serializer_context(self):
		return {
			'date': datetime.today().weekday(),
			'time': datetime.time(datetime.now())
			}
