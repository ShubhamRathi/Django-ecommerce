import stripe
import random
import hashlib
from .models import UserStripe,EmailConfirmed
from django.conf import settings
from django.contrib.auth.signals import user_logged_in
from django.db.models.signals import post_save



stripe.api_key = settings.STRIPE_SECRET_KEY

try:	
	from django.contrib.auth import get_user_model
	User = settings.AUTH_USER_MODEL
	#print "Hello"
except ImportError:
	from django.contrib.auth.models import User

def get_create_stripe(user): 	
	new_user_stripe, created = UserStripe.objects.get_or_create(user=user)
	if created:
		customer = stripe.Customer.create(
  			email = str(user.email)
		)
		#print customer
		new_user_stripe.stripe_id = customer.id
		new_user_stripe.save()


def user_created(sender, instance, created, *args, **kwargs):
	user = instance
	if created:
		get_create_stripe(user)
		email_confirmed, email_is_created = EmailConfirmed.objects.get_or_create(user=user)
		if email_is_created:
			short_hash = hashlib.sha1(str(random.random())).hexdigest()[:5]
			base, domain = str(user.email).split("@")
			activation_key = hashlib.sha1(short_hash+base).hexdigest()
			email_confirmed.activation_key = activation_key
			email_confirmed.save()
			email_confirmed.activate_user_email()

post_save.connect(user_created, sender=settings.AUTH_USER_MODEL)