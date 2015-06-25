from django.db import models
from products.models import Product
# Create your models here.

class CartItem(models.Model):
	cart = models.ForeignKey('Cart', null=True, blank=True)
	product = models.ForeignKey(Product)
	line_total = models.DecimalField(default=10.99, max_digits=1000, decimal_places=2)
	notes = models.TextField(null=True, blank=True)
	quantity = models.IntegerField(default=1)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, null=True )
	updated = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

	def __unicode__(self):
		try:
			return str(self.cart.id)
		except:
			return (self.product.title)

class Cart(models.Model):
	#items = models.ManyToManyField(CartItem, null=True, blank=True)
	#products = models.ManyToManyField(Product, null=True, blank=True)	
	total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	active = models.BooleanField(default=True)

	def __unicode__(self):
		return "Cart id: %s" %(self.id)