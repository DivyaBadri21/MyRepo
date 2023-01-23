from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.retrieve_view,name='retrieve_view'),
    path('create/',views.create_view,name='create_view'),
    path('update/<id>',views.update_view,name='update_view'),
    path('delete/<id>',views.delete_view,name='delete_view'),

]