from __future__ import unicode_literals

from django.db import models

import bcrypt
import re

# Create your models here.
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]+$')
NAME = re.compile(r'[0,1,2,3,4,5,6,7,8,9]')

class UserManager(models.Manager):
	def regist(self, firstname, lastname,email,password):
		try:
			repeat = self.filter(email__iexact = email)[0]
			if repeat.email == email:
				print repeat.email
				print email
				print "can't register this user"
				return False
		except:
			hashed_pw = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
			self.create(first_name = firstname, last_name = lastname, email = email, password = hashed_pw)
			return self.filter(email = email)[0]

	def login(self, email, password):
		activeU = self.filter(email__iexact = email)
		#  gets return a list
		if activeU and bcrypt.hashpw(password.encode("utf-8") , activeU[0].password.encode("utf-8")) == activeU[0].password:
			#should be classified as a succesful login
			return activeU[0]
		else:
			return False


class User(models.Model):
	first_name = models.CharField(max_length=45)
	last_name = models.CharField(max_length=45)
	email = models.EmailField()
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	userManager = UserManager()

