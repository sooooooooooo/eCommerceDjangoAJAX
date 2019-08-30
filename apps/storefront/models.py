##### storefront app #####
from django.db import models
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PW_REDEX = re.compile(r'(?=^.{8,}$)((?=.*\w)(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[|!"$%&\/\(\)\?\^\'\\\+\-\*]))^.*')


# Create your models here.
class CustomerManager(models.Manager):
	def validatorCusReg(self, postData):
		errors = {}
		if len(postData["fname"]) == 0:
			errors["fname"] = "The First Name field is required"
		if len(postData["lname"]) == 0:
			errors["lname"] = "The Last Name field is required"
		if len(postData["email"]) == 0:
			errors["email"] = "The Email field is required"
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
			check_email_availability = Customer.objects.filter(email = postData["email"])
			if len(check_email_availability) > 0:
				errors["email"] = "Email already exist"

		if len(postData["password"]) > 0 and not PW_REDEX.match(postData["password"]):
			errors["password"] = "Password must have a minimum length of 8, at least one uppercase letter, at least one lowercase letter, at least one number, at least one special character"
		if len(postData["password"]) > 0 and postData["confirmpassword"] != postData["password"]:
			errors["confirmpassword"] = "Passwords must match"

		return errors

	def validatorCusLogin(self, postData):
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
				check_existence = Customer.objects.get(email = postData["email"])
				if Customer.objects.get(email = postData["email"]):
					print("\n\n\n","check_existence['password']", check_existence.password)
					if not bcrypt.checkpw(postData["password"].encode(), check_existence.password.encode()):
						errors["login"] = "You cannot be logged in"
			except:
				errors["login"] = "You cannot be logged in"
		return errors

class Customer(models.Model):
	first_name = models.CharField(max_length = 255)
	last_name = models.CharField(max_length = 255)
	email = models.CharField(max_length = 255)
	password = models.CharField(max_length = 60)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = CustomerManager()










