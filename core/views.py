from django.shortcuts import render
from . models import Userdetail

# Create your views here.

def create(request):
    if request.POST:
        name=request.POST.get('name')
        age=request.POST.get('age')
        place=request.POST.get('place')
        user_obj=Userdetail(name=name,age=age,place=place)
        user_obj.save()

    return render(request,'create.html')

def home(request):
    userdata=Userdetail.objects.all()
    print(userdata)
    return render(request,'home.html',{'user':userdata})
