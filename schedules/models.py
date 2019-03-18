from django.db import models

from cafeterias.models import Cafeteria


class Schedule(models.Model):
	open_time = models.TimeField()
	close_time = models.TimeField()
	cafe = models.ForeignKey(Cafeteria, on_delete=None, db_column="cafe")
	week_day = models.PositiveSmallIntegerField()
