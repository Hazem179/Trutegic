from django.contrib import admin
from .models import Customer
# Register your models here.
@admin.register(Customer)
class CustomersAdmin(admin.ModelAdmin):
    list_display = ('name','email','phone','created_at')
