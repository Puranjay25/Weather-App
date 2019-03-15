#this file is not used
from django.db import models

# Create your models here.
class city(models.Model):
	city_name=models.TextField()

	def __init__(self):
		reutrn self.city_name
