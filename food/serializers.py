from rest_framework import serializers

from food.models import FoodProps


class FoodItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = FoodProps
		fields = (
			'weight', 'name', 'price', 'cal',
			'fat', 'carbohydrats', 'proteins', 'image'
			)
