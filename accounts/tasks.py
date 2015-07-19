from .celery import app
from .models import activate_user_email
from django.core.mail import send_mail

@app.task
	def email_user(self, subject, message, from_email=None, **kwargs):
		send_mail(subject, message, from_email, [self.user.email], kwargs)
