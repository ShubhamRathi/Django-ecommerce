from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.
from .models import Cart, CartItem
from products.models import Product

def view(request):
	try:
		the_id = request.session['cart_id']
	except:
		the_id=None
	if the_id:
		cart=Cart.objects.get(id=the_id)
		context={"cart":cart}
	else:
		empty_message ="Cart is empty. Please continue shopping"
		context={"empty":True, "empty_message": empty_message}

	template = "cart/view.html"

	return render(request, template, context)

def update_cart(request, slug):	
	request.session.set_expiry(12000)
	try:
		qty= request.GET.get('qty')
		update_qty= True
	except:
		qty=None
		update_qty= False

	notes ={}
	try:
		color= request.GET.get('color')
		notes['color']=color
	except:
		color=None

	try:
		size= request.GET.get('size')
		notes['size']=size
	except:
		size=None
	try:
		the_id = request.session['cart_id']
		#print "28. the_id: ", the_id
	except:
		new_cart=Cart()
		#print new_cart
		#print "^new_cart____________"
		new_cart.save()
		request.session['cart_id']=new_cart.id
		#print "35. request.session['cart_id']: "
		#print request.session['cart_id']
		the_id=new_cart.id
		#print "37. new_cart.id: "
		#print new_cart.id
	#print request.GET
	try:
		#print "39. slug: ", slug
		product = Product.objects.get(slug=slug)
		#print "41. product: ", product
	except Product.DoesNotExist:
		pass
	except:
		pass
	cart = Cart.objects.get(id=the_id)	
	cart_item, created=CartItem.objects.get_or_create(cart=cart, product=product)
	
	if update_qty and qty:
		if int(qty)<=0:
			cart_item.delete()
		else:
			cart_item.quantity=qty
			cart_item.notes=notes
			cart_item.save()
	else:
		pass
	# if not cart_item in cart.items.all():
	# 	cart.items.add(cart_item)
	# else:
	# 	cart.items.remove(cart_item)
	new_total=0.00
	#print "67. cart.cartitem_set.all(): ", cart.cartitem_set.all()
	#print "68. cart: ", cart
	for item in cart.cartitem_set.all():
		#print "70. item: ", item
		line_total= float(item.product.price) * item.quantity
		new_total += line_total

	cart.total= new_total
	cart.save()
	request.session['items_total'] = cart.cartitem_set.count()
	return HttpResponseRedirect(reverse("cart"))


