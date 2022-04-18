from django.shortcuts import render, redirect
from .models import Advisor,AvailableTimes
from dashboard.models import Team
from .forms import CustomerForm,ConsultationForm


# Create your views here.

def home(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            form.save()
            return redirect('main:home')
        else:
            print(form.errors)
    else:
        return render(request, 'main/home.html', {'section': 'home'})


def about(request):
    return render(request, 'main/about.html', {'section': 'about'})


def contact(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            form.save()
            return redirect('main:contact')
        else:
            print(form.errors)
    else:
        form = CustomerForm()
    return render(request, 'main/contact.html', {'section': 'contact', 'from': form})


def partnership(request):
    return render(request, 'main/partnership.html', {'section': 'partnership'})


def services(request):
    all = Advisor.objects.all()[0]
    print(all.times.all())
    return render(request, 'main/services.html', {'section': 'service'})


def team(request):
    team = Team.objects.all().order_by('id')
    print(team)

    return render(request, 'main/team.html', {'section': 'team', 'team': team})


def consultation(request):
    if request.method == 'POST':
        form = ConsultationForm(request.POST)
        if form.is_valid():
            print(form['reservation'].value())
        else:
            print(form.errors)

    return render(request, 'main/consultation.html', {'section': 'consultation'})


