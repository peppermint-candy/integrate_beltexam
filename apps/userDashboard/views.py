from django.shortcuts import render, redirect, HttpResponse
from .models import User
from .forms import RegisterForm, LoginForm, editInfo, changePw
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
	return render( request, "userdash_main.html")

def login(request):
	form = LoginForm()
	context = {
		"loginForm" : form
	}

	return render(request, "login.html", context)
def register(request):
	form = RegisterForm()
	context = {
		"regForm" : form
	}
	return render(request, "register.html", context)

def processLogin(request):
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			login = User.userManager.login(form.cleaned_data['email'],form.cleaned_data['password'])
			if login:
				request.session['id'] = login.id
				request.session['act_user'] = login.first_name
				return redirect(reverse('dashboard'))
		else:
			return HttpResponse ("wrong password, please try again")

def processRegist(request):
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			regist = User.userManager.regist(form.cleaned_data['first_name'],form.cleaned_data['last_name'],form.cleaned_data['email'],form.cleaned_data['password'])
			request.session['id'] = regist.id
			request.session['act_user'] = regist.first_name
			return redirect(reverse('dashboard'))
		else: return HttpResponse("email already exist")
	else:
		return HttpResponse("something wrong with your submission")
	
def dashboard(request):
	context = {
		"users" : User.userManager.all()
	}
	return render(request,"dashboard.html", context)

def edit(request, id):
	if request.method == "GET":
		if int(id) == int(request.session['id']):
			info = editInfo()
			pw = changePw()
			context = {
				"users" : User.userManager.all().filter(id = id)[0],
				"editEmail" : info,
				"changePw"	: pw
			}
			return render ( request, "edit.html", context)
		else: 
			return redirect(reverse("dashboard"))

def proedit(request,id):
	if request.method == "POST":
		editinfo = editInfo(request.POST)
		chpw = changePw(request.POST)
		print "method is post"
		print editinfo.errors
		if editinfo.is_valid():
			print 'form is valid'
			edit = User.userManager.filter(id=id).update(
				first_name = request.POST['first_name'],
				last_name = request.POST['last_name'],
				email = request.POST['email'])
			return redirect(reverse('dashboard'))
		else:
			print "command wasn't here"
			return redirect(reverse('dashboard'))
		if chpw.is_valid():
			editpw = User.userManager.filter(id=id).update(password = request.POST['password'])
	else:
		HttpResponse("doesn't comein with post")

def show(request,id):
	context = {
		"user" : User.userManager.all().filter(id=id)[0]
	}
	return render(request, "show.html", context)

def signout(request):
	request.session.clear()
	return redirect(reverse('usermain'))
