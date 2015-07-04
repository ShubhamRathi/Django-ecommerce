from django.contrib import admin
from .models import UserStripe, EmailConfirmed

admin.site.register(UserStripe)
admin.site.register(EmailConfirmed)