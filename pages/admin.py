from django.contrib import admin
from .models import Customer,Advisor,AvailableTimes,Reservation
# Register your models here.


@admin.register(Customer)
class CustomersAdmin(admin.ModelAdmin):
    list_display = ('name','email','phone','created_at')



@admin.register(Advisor)
class AdvisorAdmin(admin.ModelAdmin):
    list_display = ('name','type','email')


@admin.register(AvailableTimes)
class AvailableTimesAdmin(admin.ModelAdmin):
    list_display = ('week_day','from_hour','to_hour','advisor','state')
    list_editable = ('from_hour','to_hour','state')
    list_filter = ['advisor','state']



@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ['id','customer','advisor','time']




