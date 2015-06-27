import time
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect
from .models import Order
from carts.models import Cart


def checkout(request):
	
	try:
		the_id = request.session['cart_id']		
		cart = Cart.objects.get(id=the_id)		
	except:
		the_id = None
		return HttpResponseRedirect(reverse("cart"))

	new_order, created = Order.objects.get_or_create(cart=cart)
	print created

	if created:
		new_order.order_id = str(time.time())
		new_order.save()

	if new_order.status == "Finished":
		cart.delete()
		del request.session['cart_id']
		del request.session['items_total']
		return HttpResponseRedirect(reverse("cart"))

	context = {}
	template = "products/home.html"

	return render(request, template, context)
		
