from django.shortcuts import render, redirect

# Create your views here.
from typing import Any

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from productapp.models import Product

from django.contrib.auth import authenticate as auth

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
    
#to do    
#def productcreate(request,id):  # HTTPRequest / HTTPResponse
    #product = Product.objects.get(pk=id)
    #return render(request, 'productapp/product_detail.html', {'product': product})  # HTTPResponse
    

#to_do
# def index(request : Any) :  # HTTPRequest / HTTPResponse
# return render(request, 'productapp/index.html')


'''


def login(request):
    if request.user.is_authenticated():
        return redirect('base.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('base.html')
        else:
            print('Invalid login credentials')
    return render(request, 'login.html')


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
    fields = ['name', 'price', 'quantity', 'description', 'category']
    template_name = 'productapp/product_new.html'
    success_url = reverse_lazy('productapp:productlist')


class ProductUpdate(UpdateView):
    model = Product
    fields = ['name', 'price', 'quantity', 'description', 'category']
    template_name = 'productapp/product_update.html'
    success_url = reverse_lazy('productapp:productlist')


class ProductDelete(DeleteView):
    template_name = 'productapp/product_delete_confirmation.html'
    model = Product
    context_object_name = 'products'
    success_url = reverse_lazy('productapp:productlist')

