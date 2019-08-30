##### login_reg_app #####
from django.db import models
import os
from datetime import datetime, timedelta
from time import localtime, tzset, gmtime, mktime
from calendar import timegm
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PW_REDEX = re.compile(r'(?=^.{8,}$)((?=.*\w)(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[|!"$%&\/\(\)\?\^\'\\\+\-\*]))^.*')

# Create your models here.
class UserManager(models.Manager):
	def validatorReg(self, postData):
		os.environ["TZ"] = "America/Chicago"
		tzset()
		errors = {}
		if len(postData["fname"]) == 0:
			errors["fname"] = "The First Name field is required"
		if len(postData["lname"]) == 0:
			errors["lname"] = "The Last Name field is required"
		if len(postData["email"]) == 0:
			errors["email"] = "The Email field is required"
		if len(postData["alias"]) == 0:
			errors["alias"] = "The Alias field is required"
		if len(postData["dob"]) == 0:
			errors["dob"] = "The Date of Birth field is required"
		if len(postData["password"]) == 0:
			errors["password"] = "The Password field is required"
		if len(postData["confirmpassword"]) == 0:
			errors["confirmpassword"] = "The Confirm password field is required"

		if len(postData["fname"]) < 2 and len(postData["fname"]) > 0:
			errors["fname_two"] = "First Name should be at least 2 characters"
		if len(postData["fname"]) > 0 and not postData["fname"].isalpha():
			errors["fname_letter"] = "First Name should be only letters"

		if len(postData["lname"]) < 2 and len(postData["lname"]) > 0:
			errors["lname_two"] = "Last Name should be at least 2 characters"
		if len(postData["lname"]) > 0 and not postData["lname"].isalpha():
			errors["lname_letter"] = "Last Name should be only letters"

		if len(postData["email"]) > 0 and not EMAIL_REGEX.match(postData["email"]):
			errors["email"] = "Invalid email address"
		if EMAIL_REGEX.match(postData["email"]):
			check_email_availability = User.objects.filter(email = postData["email"])
			if len(check_email_availability) > 0:
				errors["email"] = "Email already exist"

		if len(postData["alias"]) > 0:
			check_alias_availability = User.objects.filter(alias = postData["alias"])
			if len(check_alias_availability) > 0:
				errors["alias"] = "Alias already taken"

		if len(postData["dob"]) > 0 and (datetime.strptime(postData["dob"], "%Y-%m-%d") > datetime.now()):
			print("\n\n\ncurrent time is:", datetime.now(), "\ndob is:", datetime.strptime(postData["dob"], "%Y-%m-%d"))
			errors["dob"] = "Date of Birth should be in the past"
		if len(postData["dob"]) > 0 and (datetime.strptime(postData["dob"], "%Y-%m-%d") < datetime.now()):
			current_date = datetime.now()
			age_checkpoint = current_date - timedelta(days = 4745)
			if datetime.strptime(postData["dob"], "%Y-%m-%d") > age_checkpoint:
				errors["dob"] = "Must be at least 13 years old to register"

		if len(postData["password"]) > 0 and not PW_REDEX.match(postData["password"]):
			errors["password"] = "Password must have a minimum length of 8, at least one uppercase letter, at least one lowercase letter, at least one number, at least one special character"
		if len(postData["password"]) > 0 and postData["confirmpassword"] != postData["password"]:
			errors["confirmpassword"] = "Passwords must match"

		return errors

	def validatorLogin(self, postData):
		os.environ["TZ"] = "America/Chicago"
		tzset()
		errors = {}
		if len(postData["email"]) == 0 and len(postData["password"]) == 0:
			errors["login"] = "Please tell us your email and password"
		if len(postData["email"]) == 0 and len(postData["password"]) != 0:
			errors["login"] = "Please tell us your email"
		if len(postData["email"]) != 0 and len(postData["password"]) == 0:
			errors["login"] = "Please tell us your password"
		if len(postData["email"]) != 0 and len(postData["password"]) != 0:
			try:
				print("\n\n\ngot into try block")
				check_existence = User.objects.get(email = postData["email"])
				if User.objects.get(email = postData["email"]):
					print("\n\n\n","check_existence['password']", check_existence.password)
					if not bcrypt.checkpw(postData["password"].encode(), check_existence.password.encode()):
						errors["login"] = "You cannot be logged in"
			except:
				errors["login"] = "You cannot be logged in"
		return errors


class User(models.Model):
	first_name = models.CharField(max_length = 255)
	last_name = models.CharField(max_length = 255)
	alias = models.CharField(max_length = 255)
	email = models.CharField(max_length = 255)
	dob = models.DateField()
	password = models.CharField(max_length = 60)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = UserManager()



