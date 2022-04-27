from django.shortcuts import render, redirect, HttpResponse
from .models import AvailableTimes, CONSULTATIONS, AdvisorType
from dashboard.models import Team
from django.forms import ValidationError
from .forms import CustomerForm, ConsultationForm
from django.http import HttpResponse, JsonResponse
import json
from .utils import available_days_filter,date_for_weekday


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
            return HttpResponse(form.errors.values())
    else:
        form = CustomerForm()
    return render(request, 'main/contact.html', {'section': 'contact', 'from': form})


def partnership(request):
    return render(request, 'main/partnership.html', {'section': 'partnership'})


def services(request):
    return render(request, 'main/services.html', {'section': 'services'})


def team(request):
    team = Team.objects.all().order_by('id')
    print(team)
    return render(request, 'main/team.html', {'section': 'team', 'team': team})


# def consultation(request):
#     av_times = AvailableTimes.objects.filter(state='available')
#     day = str(av_times.values_list('day',flat=True)[0])
#     from_hour = str(av_times.values_list('from_hour', flat=True)[0].strftime("%H:%M"))
#     to_hour = str(av_times.values_list('to_hour', flat=True)[0].strftime("%H:%M"))
#     if request.method == 'POST':
#         print(request.POST)
#         form = ConsultationForm(request.POST)
#         if form.is_valid():
#             print(form['reservation'].value())
#             form.save()
#         else:
#             print(form.errors)
#
#     return render(request, 'main/consultation.html', {'section': 'consultation','consultations':CONSULTATIONS,'day':day,'from':from_hour,'to':to_hour})
#

def consultation(request):
    if request.method == 'POST':
        form = ConsultationForm(request.POST)
        if 'submit_form' in request.POST and form.is_valid():
            form.save()
            return redirect('main:home')
        else:
            jsonData = json.loads(request.body)
            adv = jsonData.get('type')
            type_id = AdvisorType.objects.get(adv_type=adv).id
            times = available_days_filter(type_id)
            return JsonResponse({'av_dates': times})

    return render(request, 'main/consultation.html',
                  {'section': 'consultation', 'consultations': CONSULTATIONS,})


def entrepreneurship(request):
    return render(request,'internal/entrepreneurship.html',{'section': 'service'})


def marketing(request):
    return render(request,'internal/marketing.html',{'section': 'service'})

def sw_development(request):
    return render(request,'internal/software-development.html',{'section': 'service'})