from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Country

from django.template import RequestContext

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.db.models import Q

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
		return render(request, 'geoquiz/login.html', {"error_message": error_message})

	login(request,user)

	return redirect('/')


def logout_user(request):
	#add in a line to check if someone is actually logged in. If not, just redirect/render home page. Don't want logout message appearing if no logout happened.
	logout(request)

	logout_message = "You've successfully logged out."
	return render(request, 'geoquiz/home.html', {"logout_message": logout_message})

def list(request):
	if not request.user.is_authenticated():
		error_message = "Please log in first"
		return render(request, 'geoquiz/login.html', {'error_message': error_message})

	all_countries = Country.objects.all()

	search = request.GET.get('search')

	if search:
		all_countries = all_countries.filter(Q(name__icontains=search) | Q(capital__icontains=search))

	paginator = Paginator(all_countries,10)

	page = request.GET.get('page')

	try:
		all_countries = paginator.page(page)
	except PageNotAnInteger:
		all_countries = paginator.page(1)
	except EmptyPage:
		all_countries = paginator.page(paginator.num_pages)

	return render(request, 'geoquiz/list.html', {"all_countries": all_countries})

def quiz(request):
	if not request.user.is_authenticated():
		error_message = "Please log in first"
		return render(request, 'geoquiz/login.html', {'error_message': error_message})

	return render(request, 'geoquiz/quiz.html', {})

def run_quiz(request):
	if not request.user.is_authenticated():
		return redirect('/login')

	question_categories = {u'1':'Country to Capital', u'2':'Country to Flag', u'3':'Capital to Country', u'4':'Capital to Flag', u'5':'Flag to Country', u'6':'Flag to Capital'}

	if request.method != 'POST':
		region = request.GET.get('region')
		print region
		question_type = question_categories[request.GET.get('question_type')]
		print question_type

		return render(request, 'geoquiz/run_quiz.html', {'region': region, 'question_type': question_type})

	answer = request.POST['answer']
	print answer
	return HttpResponse("question answered")
