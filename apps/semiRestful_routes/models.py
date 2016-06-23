from __future__ import unicode_literals

from django.db import models

class ProductsManager(models.Manager):
	def add(self, product, desc, pc ):
		errors = {}
		
		try:
			product = self.get(product_name = product)
			errors['invalid'] = "invalid command please try again"
			return (False, errors )
		except:
			self.create( product_name = product, product_desc = desc, product_pc = pc)
			return (True, self.filter(product_name = product)[0])
			


# Create your models here.
class Products(models.Model):
	product_name = models.CharField(max_length = 45)
	product_desc = models.CharField(max_length = 255)
	product_pc = models.DecimalField(max_digits=5, decimal_places=2)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	#super set of objects (its got everything objects has + login and register)
	productManager = ProductsManager()


		