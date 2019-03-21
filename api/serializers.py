from datetime import datetime

from rest_framework import serializers
from django.db.models import Q

from cafeterias.models import Cafeteria, CafeteriaImage
from schedules.models import Schedule
from categories.models import Category
from food.models import FoodItem, FoodProps


class CafeteriaSerializer(serializers.ModelSerializer):
	images = serializers.SerializerMethodField('get_image')

	def get_image(self, cafe):
		return [i.image for i in CafeteriaImage.objects.filter(Q(cafe=cafe))]

	class Meta:
		model = Cafeteria
		fields = ('id', 'name', 'images',)


class FoodItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = FoodProps
		fields = (
			'weight', 'name', 'price', 'cal',
			'fat', 'carbohydrats', 'proteins', 'image'
			)


class ScheduleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Schedule
		fields = ('id', 'open_time', 'close_time', 'week_day', 'cafe_id',)


class CategorySerializer(serializers.ModelSerializer):
	meals = serializers.SerializerMethodField('food_list')

	def food_list(self, cat):
		return FoodItemSerializer(
			[i.props for i in FoodItem.objects.filter(Q(cat_id=cat.id))],
			many=True).data

	class Meta:
		model = Category
		fields = ('name', 'meals')


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
