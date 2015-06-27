import time
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect
from .models import Order


def checkout(request):
	
	try:
		the_id = request.session['cart_id']
		print "the_id: ", the_id
		cart = Cart.objects.get(id=the_id)
		print "Cart is:", cart
	except:
		the_id = None
		return HttpResponseRedirect(reverse("cart"))

	new_order, created = Order.objects.get_or_create(cart=cart)
	print created

	if created:
		new_order.order_id = str(time.time())
		new_order.save()

	if new_order.status == "Finished":
		del request.session['cart_id']

	context = {}
	template = "orders/home.html"

	return render(request, template, context)
		#return HttpResponseRedirect("/cart/")
		
