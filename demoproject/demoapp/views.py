from django.http import HttpResponse
from django.shortcuts import render
from . models import place
from . models import members

# Create your views here.
def index(request):
    obj=place.objects.all()
    obj2=members.objects.all()
    return render(request,"index.html",{'result':obj,'result2':obj2})
def about(request):
    return HttpResponse("This is about page")
def contact(request):
    return render(request,"contact.html")
def details(request):
    return render(request,"details.html")
def thanks(request):
    return render(request,"thanks.html")
def form(request):
    return render(request,"form.html ")
def addition(request):
    x=int(request.GET['num1'])
    y=int(request.GET['num2'])
    z=x+y
    p=x-y
    q=x*y
    r=x/y
    return render(request,"result.html",{'add':z,'sub':p,'mul':q,'div':r})


