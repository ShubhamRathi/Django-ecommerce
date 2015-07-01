from django.db import models
#from accounts.models import UserAddress
from carts.models import Cart
# Create your models here.
from django.conf import settings

STATUS_CHOICES = (
		("Started", "Started"),
		("Abandoned", "Abandoned"),
		("Finished", "Finished"),
	)

class Order(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
	order_id = models.CharField(max_length=120, default='ABC', unique=True)
	cart = models.ForeignKey(Cart)
	status = models.CharField(max_length=120, choices=STATUS_CHOICES, default="Started")
	#shipping_address = models.ForeignKey(UserAddress, related_name='shipping_address', default=1)
	#billing_address = models.ForeignKey(UserAddress, related_name='billing_address', default=1)
	sub_total = models.DecimalField(default=10.99, max_digits=1000, decimal_places=2)
	tax_total = models.DecimalField(default=0.00, max_digits=1000, decimal_places=2)
	final_total = models.DecimalField(default=10.99, max_digits=1000, decimal_places=2)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return self.order_id