from django.db import models
from django.conf import settings

class UserStripe(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	stripe_id = models.CharField(max_length=120, null=True, blank=True)

	def __unicode__(self):
		return str(self.stripe_id)

