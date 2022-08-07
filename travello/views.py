from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    est=models.Destination()
    dest.id=1
    dest.name='Hyderabad'
    dest.desc='The Ethnic City'
    dest.img='destination_1.jpg'
    dest.price=500
    return render(request,'index.html',{'dest1':dest})

def view_profile(request):
    pass

def edit_profile(request):
    pass

def delete_profile(request):
    pass