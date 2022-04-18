from django import forms
from .models import Customer,Consultation




class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('name','email','message','consultation','phone')



class ConsultationForm(forms.ModelForm):
    class Meta:
        model = Consultation
        exclude = ['created_at']