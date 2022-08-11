from django.contrib import admin
from django.urls import path, include
from travello import views
from . import views

app_name='Travello'

urlpatterns = [
    path('',views.homepage),
    path('destination/<int:dest_id>',views.dest_details,name='details'),
    path('add',views.dest_add,name='add_destination')
]
