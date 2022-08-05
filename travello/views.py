from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    if request.method=="GET":
        return render(request,'login.html')
    elif request.method=='POST':
        uname=request.POST['username']
        pwd=request.POST['password']
        if uname.lower()=='admin' and pwd=='abhi123':
            return render(request,'home.html',{'username':uname})
        else:
            return HttpResponse('<h1>Invalid user</h1> ')

def view_profile(request):
    pass

def edit_profile(request):
    pass

def delete_profile(request):
    pass