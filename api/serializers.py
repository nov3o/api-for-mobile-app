from rest_framework import serializers
from django.db.models import Q

from cafeterias.models import Cafeteria, CafeteriaImage


class CafeteriaSerializer(serializers.ModelSerializer):
	images = serializers.SerializerMethodField('get_image')

	def get_image(self, cafe):
		return [i.image for i in CafeteriaImage.objects.filter(Q(cafe=cafe))]

	class Meta:
		model = Cafeteria
		fields = ('id', 'name', 'images')
