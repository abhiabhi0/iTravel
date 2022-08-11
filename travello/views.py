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

def dest_details(request,dest_id):
    dest=list(Destination.objects.filter(id=dest_id))
    if dest:
        d = request.COOKIES.setdefault('recent_destinations', '')
        if dest.name not in d.split('\n'):
            d = d+'\n'+dest.name
            d = d.strip('\n')
        response = render(request, 'destination.html', {'dest':dest})
        response.set_cookies('recent_destinations', d)
        return response

def dest_add(request):
    if request.method=='POST':
        form = DestinationForm(request.POST,request.FILES)
        print(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            messages.info(request,'Error while creating Destination')
    return render(request,'destinationForm.html',{'form':DestinationForm()})

