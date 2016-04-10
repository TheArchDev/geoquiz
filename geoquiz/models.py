#used in the api function
import requests

from django.db import models

from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.ForeignKey(User)
	#want to add in the country where the user is from. Already requested it when registering, so need to store it within views.py
	#other fields to add, address? Number of quizzes?

class Country(models.Model):
	name = models.CharField(max_length=50)
	capital = models.CharField(max_length=25)
	region = models.CharField(max_length=15)
	#still need to add an image field

class Quiz(models.Model):
	user = models.ForeignKey(User)
	#additional, non-compulsory fields to potentially add: title, description, score

class Question(models.Model):
	quiz = models.ForeignKey(Quiz)
	country = models.ForeignKey(Country)
	question_type = models.IntegerField()
	status = models.IntegerField()

#run this function within the manage.py Django shell to populate the database.
#need to i) import requests ii) from geoquiz.models import store_country_api_data etc
def store_country_api_data():

	url = 'http://restcountries.eu/rest/v1/all'

	json_data = requests.get(url).json()

	all_country_info = {}

	for country in json_data:

		if country['region'] == 'Americas' and country['subregion'] == 'Northern America':
			#all_country_info[country['name']] = [country['capital'], u'North America']
			c = Country(name=country['name'], capital=country['capital'], region=u'North America')
			c.save()
		elif country['region'] == 'Americas':
			#all_country_info[country['name']] = [country['capital'], country['subregion']]
			c = Country(name=country['name'], capital=country['capital'], region=country['subregion'])
			c.save()
		else:
			#all_country_info[country['name']] = [country['capital'], country['region']]
			c = Country(name=country['name'], capital=country['capital'], region=country['region'])
			c.save()

	# for country_name, country_info in all_country_info.items():
	# 	c = Country(name=country_name, capital=country_info[0], region=country_info[1])
	# 	c.save()

def change_empty_capitals():
	no_capital_countries = Country.objects.all().filter(capital='')
	for country in no_capital_countries:
		country.capital = 'NO CAPITAL'
		country.save()

