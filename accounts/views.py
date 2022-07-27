from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django import template
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import Order_Form, CreateUserForm
from .decorators import unauthenticated_user, allowed_user, admin_role

# Create your views here.

@unauthenticated_user	
def register_user(request):
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)

		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')

			messages.success(request, 'Accunt was created for ' + username)
			return redirect('login')

	context = {'form':form}
	return render(request, 'accounts/register.html', context)

@unauthenticated_user
def login_user(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'Username Or Password is inccorect')

	context = {}
	return render(request, 'accounts/login.html', context)

def logout_user(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
@admin_role
def home(request):
	orders = Order.objects.all()
	customer = Customer.objects.all()
	total_customer = customer.count()
	total_order = orders.count()
	delivered = orders.filter(status='Delivered').count()
	panding = orders.filter(status='Panding').count()
	context = {'orders':orders, 'customer':customer, 'total_customer':total_customer, 'total_order':total_order, 'delivered':delivered, 'panding':panding}
	return render(request, 'accounts/dashboard.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def products(request):
	products = Product.objects.all()
	return render(request, 'accounts/products.html', {'products':products})

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def customer(request):
	customer = Customer.objects.all()
	context = {'customer':customer}
	return render(request, 'accounts/customer.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def customer_view(request, pk_test):
	customer = Customer.objects.get(id=pk_test)
	orders = customer.order_set.all()
	order_count = orders.count()
	context = {'customer':customer, 'orders':orders, 'order_count':order_count}
	return render(request, 'accounts/customer_view.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def create_order(request):
	form = Order_Form()
	if request.method == 'POST':
		form = Order_Form(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	context = {'form':form}
	return render(request, 'accounts/order_form.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def update_order(request, pk):
	order = Order.objects.get(id=pk)
	form = Order_Form(instance=order)
	if request.method == 'POST':
		form = Order_Form(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('/')
	context = {'form':form}
	return render(request, 'accounts/order_form.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def remove_order(request, pk):
	order = Order.objects.get(id=pk)
	if request.method == 'POST':
		order.delete()
		return redirect('/')
	context = {'item':order}
	return render(request, 'accounts/remove_order.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['customer'])
def user_page(request):
	orders = request.user.customer.order_set.all()
	total_order = orders.count()
	delivered = orders.filter(status='Delivered').count()
	panding = orders.filter(status='Panding').count()
	context = {'orders':orders, 'total_order':total_order, 'delivered':delivered, 'panding':panding}
	return render(request, 'accounts/user.html', context)
