from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return render(request,'index.html')

def view_profile(request):
    pass

def edit_profile(request):
    pass

def delete_profile(request):
    pass