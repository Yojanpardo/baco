from django.db import models

# Create your models here

class Product(models.Model):
	name = models.CharField(max_length=20)
	price = models.DecimalField(max_digits=7, decimal_places=2)
	description= models.CharField(max_length=255)
	category = models.CharField(max_length=144)

	def __str__(self):
		return self.name