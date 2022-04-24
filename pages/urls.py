from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('partnership/', views.partnership, name='partnership'),
    path('services/', views.services, name='services'),
    path('team/', views.team, name='team'),
    path('consultation/',views.consultation,name = 'consultation'),
    path('services/entrepreneurship/',views.entrepreneurship,name = 'entrepreneurship'),
    path('services/marketing/', views.marketing, name='marketing'),
    path('services/software_development/', views.sw_development, name='software_development')


]
