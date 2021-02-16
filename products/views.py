from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView, TemplateView, DeleteView
from .models import Products, Category, AddCart
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


import json
from django.http import JsonResponse
from pymsgbox import *

# Create your views here.

def home(request):
    categories = Category.objects.all()
    products = Products.objects.all()
    context={
        'categories': categories,
        'products': products,
    }
    return render(request, 'products/home.html', context)

def show_products(request, id):
    category = Category.objects.get(id=id)
    categories = Category.objects.all()
    products = category.products_set.all()
    context = {
        'products': products,
        'categories':categories

    }
    return render(request, 'products/show_products.html', context)

class CreateProduct(LoginRequiredMixin, CreateView):
    login_url = '/accounts/register/'
    template_name = 'products/add_product.html'
    model = Products
    fields = ['name', 'price', 'image', 'description', 'category']
    success_url = '/home/'

class UpdateProduct(LoginRequiredMixin, UpdateView):
    login_url = '/accounts/register/'
    template_name = 'products/add_product.html'
    model = Products
    fields = ['name', 'price', 'image', 'description', 'category']
    success_url = '/home/'

def DeleteProduct(request, id):
    product = Products.objects.get(id=id)
    product.delete()
    return redirect('home')

class AddCategory(LoginRequiredMixin, CreateView):
    login_url = '/accounts/register/'
    template_name = 'products/add_category.html'
    model = Category
    fields = ['name']
    success_url = '/product/add/category/'

def addtocart(request, id):
    product = Products.objects.get(id=id)
    user = request.user
    cart = AddCart.objects.filter(product=product, user=user)
    context = {}
    if cart:
        context['existstatus'] = 'already'
        # messages.success(request, 'item is already in cart')
        # cart[0].delete()
        # status = 'Add to Cart'
    else:
        AddCart.objects.create(product=product, user=user)
        # status = 'Remove From Cart'
    
    count=AddCart.objects.filter(user=user).count()
    context['count']=count#, 'status':status}
    return JsonResponse(context)

def showcart(request):
    user = request.user
    cart_items = AddCart.objects.filter(user=user)
    count = len(cart_items)
    return render(request, 'products/cart.html', {'cart_items':cart_items, 'count':count})

def removecart(request, id):
    cart_item = AddCart.objects.get(id=id)
    cart_item.delete()
    return redirect('showcart')

def detailed_product(request, id):
    product = Products.objects.get(id=id)
    return render(request, 'products/detailed_product.html', {'product':product})

class DeleteCart(DeleteView):
    template_name = 'products/confirmdelete.html'
    model = AddCart
    success_url = '/product/showcart/'


# def fetch_products(request):
#     products = list(Products.objects.values())
#     return JsonResponse(products, safe=False)
