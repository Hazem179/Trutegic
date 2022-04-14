from django.shortcuts import render, redirect
from .models import Customer



# Create your views here.

def home(request):
    if request.method =='POST':
        data = request.POST
        name = data['name']
        phone = data['phone-number']
        email = data['email']
        consultation = data['consultation']
        message = data['message']
        new_customer = Customer.objects.create(name=name,phone=phone,email=email,consultation=consultation,message=message)
        new_customer.save()
        return  redirect('main:home')
    else:
        return render(request, 'main/home.html', {'section': 'home'})

    return render(request, 'main/home.html',{'section':'home'})


def about(request):
    return render(request, 'main/about.html',{'section':'about'})


def contact(request):
    if request.method =='POST':
        data = request.POST
        name = data['name']
        phone = data['phone-number']
        email = data['email']
        consultation = data['consultation']
        message = data['message']
        new_customer = Customer.objects.create(name=name,phone=phone,email=email,consultation=consultation,message=message)
        new_customer.save()
        return  redirect('main:home')
    else:
        return render(request, 'main/contact.html', {'section': 'contact'})
    return render(request, 'main/contact.html',{'section':'contact'})


def entrepreneurship(request):
    return render(request, 'main/entrepreneurship.html',{'section':'entrepreneurship'})


def services(request):
    return render(request, 'main/services.html',{'section':'service'})


def team(request):
    return render(request, 'main/team.html',{'section':'team'})
