
from django.conf.urls import url
from django.urls import path
from productapp import views
from productapp.views import ProductCreate, ProductUpdate

app_name = 'productapp'

# #URLPatterns for function based views
urlpatterns = [

#function based views urls
    #path('index/', views.index, name='index'),
    #path('', views.index, name='index'),
    #path('productlist/', views.productlist, name='productlist'),
    #path('productlist/<int:id>/', views.productdetails, name='productdetails'),
    #path('<int:id>/productdelete/', views.delete, name='productdelete'),

#class based views urls
    path('productlist/', views.ProductList.as_view(), name='productlist'),
    path('productdetail/<int:pk>/', views.ProductDetail.as_view(), name='productdetail'),
    path('productnew/', views.ProductCreate.as_view(), name='productnew'),
    path('productupdate/<int:pk>/', views.ProductUpdate.as_view(), name='productupdate'),
    path('productdelete/<int:pk>/', views.ProductDelete.as_view(), name='productdelete'),
]