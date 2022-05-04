from django.contrib import admin
from .models import Customer,Advisor,AvailableTimes,Reservation,Consultation,AdvisorType
# Register your models here.


@admin.register(Customer)
class CustomersAdmin(admin.ModelAdmin):
    list_display = ('name','email','phone','created_at')


class AvailableTimesInline(admin.TabularInline):
    model = AvailableTimes


@admin.register(Advisor)
class AdvisorAdmin(admin.ModelAdmin):
    list_display = ('name','email')
    inlines = [AvailableTimesInline,]



@admin.register(AvailableTimes)
class AvailableTimesAdmin(admin.ModelAdmin):
    list_display = ('day','from_hour','to_hour','advisor','state')
    list_editable = ('from_hour','to_hour','state')
    list_filter = ['advisor','state','day']



@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ['id','customer','advisor','time']


@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    list_display = ['name','phone','consultation']


@admin.register(AdvisorType)
class AdvisorTypeAdmin(admin.ModelAdmin):
    list_display = ['adv_type']


