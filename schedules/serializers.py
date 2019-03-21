from rest_framework import serializers

from schedules.models import Schedule


class ScheduleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Schedule
		fields = ('id', 'open_time', 'close_time', 'week_day', 'cafe_id',)
