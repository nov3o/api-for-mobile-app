from django.db import models


class Cafeteria(models.Model):
    name = models.TextField(max_length=30)

class CafeteriaImage(models.Model):
	cafe = models.ForeignKey(Cafeteria, on_delete=None, db_column="cafe")
	image = models.TextField(max_length=20) # Image name
