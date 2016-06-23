from django import forms
import re
from .models import User


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]+$')
NAME = re.compile(r'[0,1,2,3,4,5,6,7,8,9]')

class RegisterForm(forms.Form):
	first_name = forms.CharField(max_length=45)
	last_name = forms.CharField(max_length=45)
	email = forms.EmailField()
	password = forms.CharField(max_length=100, widget=forms.PasswordInput)
	confirm_password = forms.CharField(max_length=100,widget=forms.PasswordInput)

	def clean_errors(self):
		errors = {}
		data = self.cleaned_data
		if len(data["first_name"]) < 2:
			errors['first_name'] = "First Name is too short"
		if NAME.match(data["first_name"]):
			errors['name1'] = "First name cannot contain number(s)"
		if len(data["last_name"]) <2 :
			errors['last_name'] = "Last Name is too short"
		if NAME.match(data["last_name"]):
			errors['name2'] = "Last name cannot contain number(s)"
		if len(data["password"]) < 8 :
			errors['password'] = "Password is too short"
		if data["password"] != data["confirm_password"]:
			errors['confirm_password'] = "Password must match"
		if not EMAIL_REGEX.match(data["email"]):
			errors['email'] = "Please enter a valid email"
		
		if errors:
			return errors
		else:
			return data



class LoginForm(forms.Form):
	email = forms.EmailField()
	password = forms.CharField(max_length=100, widget=forms.PasswordInput)
	def clean_errors(self):
		errors = {}
		data = self.cleaned_data

		if not EMAIL_REGEX.match(data["email"]):
			errors['email'] = "Please enter a valid email"
		if errors:
			return errors
		else:
			return data

class editInfo(forms.ModelForm):
	# email = forms.EmailField()
	# first_name= forms.CharField(max_length=100)
	# last_name= forms.CharField(max_length=100)
	class Meta:
		model = User
		fields = ['first_name','last_name','email']

class changePw(forms.ModelForm):
	class Meta:
		model = User
		fields =['password']



	# def clean_errors(self):
	# 	data = self.cleaned_data
	# 	if len(data["first_name"]) < 2:
	# 		errors['first_name'] = "First Name is too short"
	# 	if NAME.match(data["first_name"]):
	# 		errors['name1'] = "First name cannot contain number(s)"
	# 	if len(data["last_name"]) <2 :
	# 		errors['last_name'] = "Last Name is too short"
	# 	if NAME.match(data["last_name"]):
	# 		errors['name2'] = "Last name cannot contain number(s)"

	# 	if errors:
	# 		return	errors
	# 	else:
			# return data