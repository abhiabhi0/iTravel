from django.contrib import admin
from django.urls import path, include
from travello import views
from . import views

urlpatterns = [
    path('',views.homepage),
    path('view',views.view_profile),
    path('edit',views.edit_profile),
    path('delete',views.delete_profile),
]
