from django.db import models

from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.ForeignKey(User)

class Country(models.Model):
	name = models.CharField(max_length=50)
	capital = models.CharField(max_length=25)
	continent = models.CharField(max_length=15)
	#still need to add an image field

#class Question(models.Model):

