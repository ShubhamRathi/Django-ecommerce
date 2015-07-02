from django.shortcuts import render, HttpResponseRedirect, Http404
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from .forms import LoginForm, RegistrationForm

def logout_view(request):
	logout(request)
	return HttpResponseRedirect("/")

def login_view(request):
	form = LoginForm(request.POST or None)
	btn = "Login"
	if form.is_valid():
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		user = authenticate(username=username, password=password)
		login(request, user)
		messages.success(request, "Successfully Logged In. Welcome Back!")
		return HttpResponseRedirect("/")
	context = {
		"form": form,
		"submit_btn": btn,
	}
	return render(request, "form.html", context)

def registration_view(request):
	form = RegistrationForm(request.POST or None)
	btn = "Join"
	if form.is_valid():
		new_user = form.save(commit=False)
		# new_user.first_name = "Justin" this is where you can do stuff with the model form
		new_user.save()
		messages.success(request, "Successfully Registered. Please confirm your email now.")
		return HttpResponseRedirect("/")
		# username = form.cleaned_data['username']
		# password = form.cleaned_data['password']
		# user = authenticate(username=username, password=password)
		# login(request, user)

	context = {
		 "form": form,
		 "submit_btn": btn,
	}
	return render(request, "form.html", context)