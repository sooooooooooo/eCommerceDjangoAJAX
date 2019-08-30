##### login_reg_app #####
from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
import os
from datetime import datetime, timedelta
from time import localtime, tzset, gmtime, mktime
from calendar import timegm
import bcrypt
import re
from requests import get

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PW_REDEX = re.compile(r'(?=^.{8,}$)((?=.*\w)(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[|!"$%&\/\(\)\?\^\'\\\+\-\*]))^.*')


# Create your views here.
# def index(request):
# 	return HttpResponse("home page")

def register(request):
	if request.method == "POST":
		errors = User.objects.validatorReg(request.POST)
		if len(errors) > 0:
			for key, value in errors.items():
				messages.error(request, value)
			request.session["fname"] = request.POST["fname"]
			request.session["lname"] = request.POST["lname"]
			request.session["email"] = request.POST["email"]
			request.session["alias"] = request.POST["alias"]
			request.session["dob"] = request.POST["dob"]
			return redirect("/adminportal/register")
		else:
			pw_hash = bcrypt.hashpw(request.POST["password"].encode(), bcrypt.gensalt())
			print(pw_hash)
			newly_registered_user = User.objects.create(first_name = request.POST["fname"], last_name = request.POST["lname"], alias = request.POST["alias"], email = request.POST["email"], dob = request.POST["dob"], password = pw_hash)
			print("\n\n\nnewly_registered_user id is:", newly_registered_user.id)
			request.session["fname"] = newly_registered_user.first_name
			request.session["user_id"] = newly_registered_user.id
			messages.success(request, "Successfully registered!")
			return redirect("/adminportal/success")
	if request.method == "GET":
		return render(request, "login_reg_app/register.html")

def success(request):
	if "fname" not in request.session:
		messages.error(request, "You must be logged in to enter the website")
		return redirect("/adminportal")
	ip = get('https://api.ipify.org').text
	print('My public IP address is: {}'.format(ip))
	context = {
		"ip": ip
	}
	return redirect("/dashboard")

def showlogin(request):
	return render(request, "login_reg_app/login.html")

def login(request):
	if request.method == "POST":
		errors = User.objects.validatorLogin(request.POST)
		if len(errors) > 0:
			for key, value in errors.items():
				messages.error(request, value)
			request.session["loginEmail"] = request.POST["email"]
			return redirect("/adminportal")
		else:
			loggedin_user = User.objects.get(email = request.POST["email"])
			request.session["fname"] = loggedin_user.first_name
			request.session["user_id"] = loggedin_user.id
			messages.success(request, "Successfully logged in!")
			return redirect("/dashboard")
	if request.method == "GET":
		return redirect("/adminportal")


def logout(request):
	if "fname" and "lname" and "email" and "dob" in request.session:
		del request.session["fname"]
		del request.session["lname"]
		del request.session["email"]
		del request.session["dob"]
	if "loginEmail" in request.session:
		del request.session["loginEmail"]
	if "fname" in request.session:
		del request.session["fname"]
	if "user_id" in request.session:
		del request.session["user_id"]
	if "alias" in request.session:
		del request.session["alias"]
	messages.success(request, "You've logged out")
	return redirect("/adminportal")






