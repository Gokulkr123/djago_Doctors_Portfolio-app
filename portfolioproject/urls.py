from django.contrib import admin
from django.urls import path
from greetings import views

urlpatterns = [
    path('', views.login_page, name='login'), 
    path('create/', views.create_data, name='createlist'),
    path('retrieve/', views.read_data, name='readlist'),
    path('home/', views.home_page, name='viewlist'),
    path('update/<int:pk>/', views.update_data, name='update'),
    path('delete/<int:pk>/', views.delete_data, name='delete'),
    path('signup/',views.signup_page,name='signup'),
    path('logout/', views.logout_view,name='logout'),
    path('aboutUs/', views.aboutUs,name='aboutus'),
]
