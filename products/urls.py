from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('product/', views.CreateProduct.as_view(), name='create_product'),
    path('product/edit/<pk>/', views.UpdateProduct.as_view(), name='edit_product'),
    path('product/delete/<int:id>/', views.DeleteProduct, name='delete_product'),
    path('product/showcart/', views.showcart, name='showcart'),
    path('product/removecart/<pk>/', views.DeleteCart.as_view(), name='removecart'),
    path('product/add/category/', views.AddCategory.as_view(), name='add_category'),
    path('product/category/<int:id>/', views.show_products, name='show_products'),
    path('product/detailed_product/<int:id>/', views.detailed_product, name='detailed_product'),
    path('product/<sort>/', views.home, name='home'),
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('product/addtocart/<int:id>/', views.addtocart, name='addtocart'),
    
]
