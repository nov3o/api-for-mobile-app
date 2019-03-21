from datetime import datetime

from rest_framework import serializers
from django.db.models import Q

from schedules.models import Schedule
from categories.models import Category

from categories.serializers import CategorySerializer


class MenuSerializer(serializers.ModelSerializer):
	menu = serializers.SerializerMethodField('resolve_menu')
	open = serializers.SerializerMethodField('is_open')

	def resolve_menu(self, sched):
		return CategorySerializer(
			Category.objects.filter(Q(sched_id=sched.id)), many=True).data

	def is_open(self, sched):
		if self.context.get("time") == None:
			return None;
		tm = datetime.time(self.context.get("time"))
		op_t = sched.open_time
		cl_t = sched.close_time
		if op_t < tm and cl_t > tm:
			return 1
		else:
			return 0

	class Meta:
		model = Schedule
		fields = (
			'id', 'open', 'open_time', 'close_time', 'week_day', 'cafe_id',
			'menu',)
