from django.http import HttpResponse #this is used when we want to show text 
from django.shortcuts import render



def homePage(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about-us.html")
def our(request):
    return render(request, "our_invester.html")
def product(request):
    return render(request, "product.html")
