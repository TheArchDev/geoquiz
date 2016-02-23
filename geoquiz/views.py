from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
#from .models import

from django.template import RequestContext

#Make a helper function that will verify if someone is logged in or not, and have a parameter that will be the URL to relocate to after they've successfully logged in??

def home(request):
	#return HttpResponse("Home page")
	return render(request, 'geoquiz/home.html', {})

#Would want to return some simple form of error message to the user, so that they know if eg that username is already taken etc
def register(request):
	if request.method != "POST":
		#return HttpResponse("Register page through GET request")
		return render(request, 'geoquiz/register.html', {})

	print request.POST
	#return HttpResponse("Register page through POST request")

	user = User.objects.create_user(first_name = request.POST['first_name'], last_name = request.POST['last_name'], username = request.POST['username'], email = request.POST['email'], password = request.POST['password'])

	if not user:
		return render(request, 'geoquiz/register.html', {})
		#NB I tried doing return redirect('/register/') instead. This still works, but it goes through urls.py then through this whole function again, rather than just going straight to the html page.

	user.save()
	
	#probably would only want to save the country, once know that the entry has been successfully added to auth_user.

	user = authenticate(username=request.POST['username'], password=request.POST['password'])
	login(request,user)

	return redirect('/')
	#check that this works correctly once I have a header showing who's currently logged in.


def login_user(request):
	if request.method != "POST":
		return render(request, 'geoquiz/login.html', {})

	user = authenticate(username=request.POST['username'], password=request.POST['password'])

	if not user:
		#get it to display some kind of temporary pop-up/message or indicator in the HTML now that
		error_message = "Invalid username/password combination"
		return render(request, 'geoquiz/login.html', {"error": error_message})

	login(request,user)

	return redirect('/')


def logout_user(request):
	#add in a line to check if someone is actually logged in. If not, just redirect/render home page. Don't want logout message appearing if no logout happened.
	logout(request)

	logout_message = "You've successfully logged out."
	return render(request, 'geoquiz/home.html', {"logout_message": logout_message})

def list(request):
	#return HttpResponse("List page")
	return render(request, 'geoquiz/list.html', {})

def quiz(request):
	#return HttpResponse("Quiz page")
	return render(request, 'geoquiz/quiz.html', {})