from django.shortcuts import render

# Create your views here.
from typing import Any

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from productapp.models import Product

'''
#function based views

def index(request):  # HTTPRequest / HTTPResponse
    return HttpResponse("Hello World!.")  # no templates yet


def productlist(request):  # HTTPRequest / HTTPResponse
    products = Product.objects.all() # Query Set Object from ORM
    return render(request,'productapp/product_list.html', {'products':products} ) #HTTPResponse
    #return HttpResponse("Product List is here!.")  # no templates yet


def productdetails(request,id):  # HTTPRequest / HTTPResponse
    product = Product.objects.get(pk=id)
    return render(request, 'productapp/product_detail.html', {'product': product})  # HTTPResponse
    

#to_do
# def index(request : Any) :  # HTTPRequest / HTTPResponse
# return render(request, 'productapp/index.html')


'''


# class based views

class ProductList(ListView):  # generic view
    template_name = 'productapp/product_list_class_view.html'
    model = Product
    context_object_name = 'products'


class ProductDetail(DetailView):
    model = Product
    template_name = 'productapp/product_detail_class_view.html'
    context_object_name = 'product'


class ProductCreate(CreateView):
    model = Product
    fields = ['name', 'price', 'quantity', 'description']
    template_name = 'productapp/product_new.html'
    success_url = reverse_lazy('productapp:product_list')


class ProductUpdate(UpdateView):
    model = Product
    fields = ['name', 'price', 'quantity', 'description']
    template_name = 'productapp/product_update.html'
    success_url = reverse_lazy('productapp:product_list')
