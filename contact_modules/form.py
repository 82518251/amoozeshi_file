from django import forms
from .models import contact

class ContactModelsForm(forms.ModelForm):
    class Meta:
        model= contact
        fields =[ 'name','email' , 'message' ,'title']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'نام',
            }),
            'email': forms.EmailInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'ایمیل'
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'موضوع تو',
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'پیغام تو',
            })
        }

    labels= {
            'name' : 'نام',
            'email' : 'ایمیل شما',
            'title' : 'موضوع تو',
            'message' : 'پیغام تو'

        }

    error_messages={
            'name' :{
            'required' : 'لطفا نام و نام خانوادگی را وارد کنید'
            }
        }