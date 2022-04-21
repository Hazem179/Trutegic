from django.shortcuts import render, redirect,HttpResponse
from .models import AvailableTimes,CONSULTATIONS
from dashboard.models import Team
from django.forms import ValidationError
from .forms import CustomerForm,ConsultationForm


# Create your views here.

def home(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:home')
    else:
        return render(request, 'main/home.html', {'section': 'home'})


def about(request):
    return render(request, 'main/about.html', {'section': 'about'})


def contact(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
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
    return render(request, 'main/services.html', {'section': 'service'})


def team(request):
    team = Team.objects.all().order_by('id')
    print(team)
    return render(request, 'main/team.html', {'section': 'team', 'team': team})


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def consultation(request):

    av_times = AvailableTimes.objects.filter(state='available')
    day = str(av_times.values_list('day',flat=True)[0])
    from_hour = str(av_times.values_list('from_hour', flat=True)[0].strftime("%H:%M"))
    to_hour = str(av_times.values_list('to_hour', flat=True)[0].strftime("%H:%M"))
    if request.method == 'POST':
        form = ConsultationForm(request.POST)
        if form.is_valid():
            print(form['reservation'].value())
            form.save()
        else:
            print(form.errors)

    return render(request, 'main/consultation.html', {'section': 'consultation','consultations':CONSULTATIONS,'day':day,'from':from_hour,'to':to_hour})


