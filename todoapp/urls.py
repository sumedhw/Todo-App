from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'todoapp'

urlpatterns = [
    path('', home , name='home'),
    path('user_registration' , user_registration , name="user_registration"),
    path('user_login' , login , name="login"),
    path('user_logout' , logout , name="logout"),

    path('create_task' , create_task , name="create_task"),
    path('store_task' , store_task , name="store_task"),
    path('delete_task/<int:id>' , delete_task , name="delete_task"),

]