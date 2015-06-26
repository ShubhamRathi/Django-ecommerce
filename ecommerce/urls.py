"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', 'products.views.home', name='home'),
    url(r'^s/$', 'products.views.search', name='search'),
    url(r'^cart/$', 'carts.views.view', name='cart'),
    url(r'^cart/(?P<id>\d+)/$', 'carts.views.remove_from_cart', name='remove_from_cart'),
    url(r'^cart/(?P<slug>[\w-]+)/$', 'carts.views.add_to_cart', name='add_to_cart'),
    url(r'^products/(?P<slug>[\w-]+)/$', 'products.views.single', name='single_product'),
    url(r'^products/$', 'products.views.all', name='products'),
    url(r'^admin/', include(admin.site.urls)),
] 

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)	 	
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
