from rest_framework import serializers
from django.db.models import Q

from food.models import FoodItem
from categories.models import Category

from food.serializers import FoodItemSerializer


class CategorySerializer(serializers.ModelSerializer):
	meals = serializers.SerializerMethodField('food_list')

	def food_list(self, cat):
		return FoodItemSerializer(
			[i.props for i in FoodItem.objects.filter(Q(cat_id=cat.id))],
			many=True).data

	class Meta:
		model = Category
		fields = ('name', 'meals')
