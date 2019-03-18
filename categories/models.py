from django.db import models

from schedules.models import Schedule


class Category(models.Model):
	name = models.TextField(max_length=20)
	sched = models.ForeignKey(Schedule, on_delete=None, db_column="sched")
