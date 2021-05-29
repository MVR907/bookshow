from django.db import models

# Create your models here.
class Book(models.Model):
	name=models.CharField(max_length=50)
	authorname=models.CharField(max_length=50)
	Summary=models.TextField()
	picture=models.ImageField()
	price=models.FloatField()

	#to display object in string
	def __str__(self):
		return self.name
