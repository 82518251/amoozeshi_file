from django import forms
from .models import ProductComment

class ProductCommentForm(forms.ModelForm):
    class Meta:
        model = ProductComment
        fields = ['name','email','text', 'image', 'rating']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':'نام شما'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل شما'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'متن شما'}),
            'rating' : forms.NumberInput(attrs={'class': 'form-control', 'min':1, 'max':5, 'placeholder': 'امتیاز شما'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'})
        }
        labels = {
            'name' : 'نام و نام خانوادگی',
            'email': 'آدرس پست الکترونیکی',
            'text':'اینجا تایپ کنید ',
            'rating': 'امتیاز شما',
            'image': 'عکس شما',

        }
    def clean(self):
        cleaned_data=super().clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')

        if not self.instance.user:
            if not name:
                raise forms.ValidationError("لطفا نام خود را وارد کنید")
            if not email:
                raise forms.ValidationError("لطفا ایمیل خود را وارد کنید")
            return cleaned_data