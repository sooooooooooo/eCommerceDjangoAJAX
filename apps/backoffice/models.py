from django.db import models

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length = 255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

class Product(models.Model):
	name = models.CharField(max_length = 255)
	description = models.TextField()
	price = models.DecimalField(max_digits=10, decimal_places=2)
	category = models.ForeignKey(Category, related_name = "products")
	inventory = models.IntegerField()
	image = models.FileField(upload_to='images/')
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)