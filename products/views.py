from django.shortcuts import render, Http404
from .models import Product, ProductImage
from django.conf import settings
from marketing.models import MarketingMessage

# Create your views here.
def home(request): # When I enter a URL, I'm making a request. This request is being handled at home.
	# print "Inside home():"
	# print request
	# print "_________________________________________" 
	print request.POST
	products = Product.objects.all()
	context = {'products': products}
	template='products/home.html'
	return render(request, template, context)


def all(request):
	products = Product.objects.all()
	context = {'products': products}
	template = 'products/all.html'	
	return render(request, template, context)

def single(request, slug):
	try:
		product = Product.objects.get(slug=slug)
		images = ProductImage.objects.filter(product=product)
		context = {'product': product, "images": images}
		template = 'products/single.html'	
		return render(request, template, context)
	except:
		return Http404
	

def search(request):
	try:
		q = request.GET.get('q')
	except:
		q = None
	
	if q:
		products = Product.objects.filter(title__icontains=q)
		context = {'query': q, 'products': products}
		template = 'products/results.html'	
	else:
		template = 'products/home.html'	
		context = {}
	return render(request, template, context)