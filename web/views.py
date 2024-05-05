from django.shortcuts import render,redirect
from .  models import contact

# Create your views here.

def index(request):
    if request.method=='POST':
      name=request.POST.get("name")
      email=request.POST.get("email")
      text=request.POST.get("text")

      contact1=contact(
         name=name,
         email=email,
         text=text,
      )
      contact1.save()
    return render(request,"web/index.html")
  
def success(request):
   return render(request,"web/tank.html")