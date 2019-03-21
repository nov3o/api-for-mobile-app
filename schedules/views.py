from django.db.models import Q
from rest_framework import generics
from datetime import datetime

from schedules.models import Schedule

from schedules.serializers import ScheduleSerializer


class CafeTodaySchedule(generics.ListAPIView):
	serializer_class = ScheduleSerializer

	def get_queryset(self):
		cid = self.kwargs['cafe_id']
		wd = datetime.today().weekday()
		return Schedule.objects.filter(Q(week_day=wd)).filter(Q(cafe_id=cid))


class AllTodaySchedules(generics.ListAPIView):
	serializer_class = ScheduleSerializer
	queryset = Schedule.objects.all()


class OneDayCafeSchedule(generics.ListAPIView):
	serializer_class = ScheduleSerializer

	def get_queryset(self):
		wd = self.kwargs['wd']
		cid = self.kwargs['cafe_id']
		return Schedule.objects.filter(Q(week_day=wd), Q(cafe_id=cid))
