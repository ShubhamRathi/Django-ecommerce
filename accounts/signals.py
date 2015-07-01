import stripe
from django.conf import settings
from django.contrib.auth.signals import user_logged_in
from .models import UserStripe

stripe.api_key = settings.STRIPE_SECRET_KEY


def get_create_stripe(sender, user, *args, **kwargs):
	new_user_stripe, created = UserStripe.objects.get_or_create(user=user)
	print "hello"
	if created:
		customer = stripe.Customer.create(
  			email = str(user.email)
		)
		print customer
		new_user_stripe.stripe_id = customer.id
		new_user_stripe.save()

user_logged_in(get_create_stripe)