from django.shortcuts import render, redirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import Products

# Create your views here.
def realindex(request):
	return render("index2.html")
def index(request):
	context = {
		"products" : Products.productManager.all()
	}

	if request.method == "GET":
		products = Products.productManager.all()
		context = {"products" : products}
		return render(request,"products/index.html", context)

	if request.method == 'POST':
		Products.productManager.create(request.POST)
		#reditrect('/products')
		return HttpResponse('Successful creation')

	return render(request, "index.html",context)

def new(request):
	if request.method == "GET":
		products = Products.productManager.get(id=id)
		context =  { "products" : products}
		return render(request, "products/show.html",context)

	if request.method == "PATCH":
		products = Products.productManager.get(id=id).update(request.POST)
		context =  { "products" : products}
		return render(request,"products/shows.html")

	if request.method == "DELETE":
		Products.productManager.filter(id=id).delete()
		return HttpResponse("Delete complete")


def showupdatedelete(request):
	if request.method == 'GET':
		#show
	if request.method == "PATCH":
		#update
	if request.method == "DELETE":
		#delete

def edit(request):
	Products.productManager.create(request.POST)
	#reditrect('/products')
	context = { "products" : products}
	return render(request,"products/edit.html",context)

def show(request):
	return render(request, "show.html")

def new(request):
	return render(request, "new.html")

def edit(request):
	return render(request, "edit.html")

def create(request):
	if request.method === 'POST':
		addnew = Products.productManager.add(request.POST['addName'],request.POST['addDesc'],request.POST['addPrice'])
		if addnew[0]:
			return redirect('/products')
		else:
			for i in addnew[1]:
				messages.info(request, addnew[1][i])
			return redirect('/products')


def update(request):
	return HttpResponse("Hello Tuesday")

def destroy(request):
	return HttpResponse("Hello Tuesday")