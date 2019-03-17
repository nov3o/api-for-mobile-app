from django.db import models

class Cafeteria(models.Model):
    name = models.TextField(max_length=30)

class Member(models.Model):
	open_time = models.TimeField()
	close_time = models.TimeField()
	cafeteria_id = models.PositiveIntegerField()
	week_day = models.PositiveSmallIntegerField()

class Category(models.Model):
	name = models.TextField(max_length=20)
	schedule_id = models.PositiveIntegerField()

class CafeteriaImage(models.Model):
	cafeteria_id = models.PositiveIntegerField()
	image = models.TextField(max_length=20) # Image name

class Macroelements(models.Model):
	proteins = models.FloatField()
	fat = models.FloatField()
	carbohydrats = models.FloatField()
	food_id = models.PositiveIntegerField()

class FoodItem(models.Model):
	name = models.TextField(max_length=40)
	weight = models.IntegerField()
	price = models.DecimalField(max_digits=5, decimal_places=2)
	# Calories per one piece
	cal = models.PositiveSmallIntegerField()
	image = models.TextField(max_length=20)
	category_id = models.PositiveIntegerField()
