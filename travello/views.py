from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    dests=Destination.objects.all()
    return render(request,'index.html',{'dests':dests})

def view_profile(request):
    pass

def edit_profile(request):
    pass

def delete_profile(request):
    pass

def user_register(request):
    return render(request,'register.html')