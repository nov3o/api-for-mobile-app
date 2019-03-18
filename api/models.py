from django.db import models

class Cafeteria(models.Model):
    name = models.TextField(max_length=30)

class CafeteriaImage(models.Model):
	cafeteria_id = models.PositiveIntegerField()
	image = models.TextField(max_length=20) # Image name

class Schedule(models.Model):
	open_time = models.TimeField()
	close_time = models.TimeField()
	cafeteria_id = models.PositiveIntegerField()
	week_day = models.PositiveSmallIntegerField()

class Category(models.Model):
	name = models.TextField(max_length=20)
	schedule_id = models.PositiveIntegerField()

class FoodItem(models.Model):
	weight = models.IntegerField()
	name = models.TextField(max_length=70)
	price = models.DecimalField(max_digits=5, decimal_places=2)
	# Calories per 100 grams
	cal = models.PositiveSmallIntegerField()
	fat = models.DecimalField(max_digits=3, decimal_places=1)
	carbohydrats = models.DecimalField(max_digits=3, decimal_places=1)
	proteins = models.DecimalField(max_digits=3, decimal_places=1)
	category_id = models.PositiveIntegerField()
	image = models.TextField(max_length=20)
