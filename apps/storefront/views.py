##### storefront app #####
from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
import bcrypt
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PW_REDEX = re.compile(r'(?=^.{8,}$)((?=.*\w)(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[|!"$%&\/\(\)\?\^\'\\\+\-\*]))^.*')



# Create your views here.
def indexStorefront(request):
	return render(request, "storefront/index.html")

def allprodStorefront(request):
	return render(request, "storefront/allproducts.html")

def readoneStorefront(request):
	return render(request, "storefront/oneproduct.html")

def checkout(request):
	return render(request, "storefront/cart.html")

def customerLogin(request):
	if request.method == "POST":
		errors = Customer.objects.validatorCusLogin(request.POST)
		if len(errors) > 0:
			for key, value in errors.items():
				messages.error(request, value)
			request.session["email_customer_login"] = request.POST["email"]
			return redirect("/login")
		else:
			logged_customer  = Customer.objects.get(email = request.POST["email"])
			request.session["customer_id"] = logged_customer.id
			request.session["customer_fname"] = logged_customer.first_name
			return redirect("/")
	if request.method == "GET":
		return render(request, "storefront/customerlogin.html")

def customerRegister(request):
	if request.method == "POST":
		errors = Customer.objects.validatorCusReg(request.POST)
		if len(errors) > 0:
			for key, value in errors.items():
				messages.error(request, value)
			request.session["fname_customer_reg"] = request.POST["fname"]
			request.session["lname_customer_reg"] = request.POST["lname"]
			request.session["email_customer_reg"] = request.POST["email"]
			return redirect("/register")
		else:
			pw_hash = bcrypt.hashpw(request.POST["password"].encode(), bcrypt.gensalt())
			print("\n\n\n", pw_hash)
			newly_registered_customer = Customer.objects.create(first_name = request.POST["fname"], last_name = request.POST["lname"], email = request.POST["email"], password = pw_hash)
			print("newly_registered_customer id:", newly_registered_customer.id)
			request.session["customer_id"] = newly_registered_customer.id
			request.session["customer_fname"] = request.POST["fname"]
			return redirect("/")
	if request.method == "GET":
		return render(request, "storefront/customerregister.html")

def customerLogout(request):
	if "customer_id" and "customer_fname" in request.session:
		del request.session["customer_id"]
		del	request.session["customer_fname"]
	if "fname_customer_reg" and "lname_customer_reg" and "email_customer_reg" in request.session:
		del request.session["fname_customer_reg"]
		del	request.session["lname_customer_reg"]
		del	request.session["email_customer_reg"]
	if "email_customer_login" in request.session:
		del request.session["email_customer_login"]
	messages.success(request, "You've logged out")
	return redirect("/login")




