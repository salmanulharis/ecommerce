from django.contrib import admin
from django.urls import path
from accounts import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('users/<sort>/', views.ListUsers.as_view()),
    path('users/detail/<pk>/', views.DetailedUser.as_view()),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.logout_fn, name='logout'),
    path('edit/user/', views.EditUser.as_view()),
    path('password/', views.ChangePassword.as_view()),
]
