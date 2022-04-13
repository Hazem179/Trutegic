from django.forms import ModelForm
from django import forms
from phonenumber_field.formfields import PhoneNumberField
from .models import Customer


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ('name', 'phone', 'email', 'message', 'consultation')
        phone =  PhoneNumberField(widget=forms.TextInput(attrs={'placeholder': 'Phone Number'})),
        widgets = {
            # 'name': forms.Textarea(attrs={'placeholder': 'Name'}),
        'name':forms.TextInput(attrs ={'placeholder': 'Name'}),
        'phone': '',
        'email':forms.EmailInput(attrs ={'placeholder': 'E-Mail'}),
        'consultation':'',
        'message':forms.Textarea(attrs ={'placeholder': 'Message'}),

        }

    # class Meta:
    #     model = Customer
    #     fields = ('name','phone','email','message','consultation')
    #
    #
    # def __init__(self,*args,**kwargs):
    #     super().__init__(*args,**kwargs)
    #     self.fields['name'].widget.attrs.update([{'placeholder': 'Name'}])
    #     self.fields['phone'].widget.attrs.update([{'placeholder': 'Phone Number'}])
    #     self.fields['email'].widget.attrs.update([{'placeholder': 'E-Mail'}])
    #     #self.fields['consultation'].widgets.attrs.update([{'placeholder': 'Name'}])
    #     self.fields['message'].widget.attrs.update([{'placeholder': 'Message'}])