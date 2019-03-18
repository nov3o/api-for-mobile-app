from django.db import models

from categories.models import Category


class FoodProps(models.Model):
	weight = models.IntegerField()
	name = models.TextField(max_length=70)
	price = models.DecimalField(max_digits=5, decimal_places=2)
	# Calories per 100 grams
	cal = models.PositiveSmallIntegerField()
	fat = models.DecimalField(max_digits=3, decimal_places=1)
	carbohydrats = models.DecimalField(max_digits=3, decimal_places=1)
	proteins = models.DecimalField(max_digits=3, decimal_places=1)
	image = models.TextField(max_length=20)

class FoodItem(models.Model):
	# props_id = models.PositiveIntegerField()
	props = models.ForeignKey(FoodProps, on_delete=None, db_column="props")
	cat = models.ForeignKey(
		Category, on_delete=None, db_column="cat"
		)
