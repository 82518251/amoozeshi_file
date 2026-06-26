from django.core import validators
from django import forms
from django.core.exceptions import ValidationError

class RegisterForm(forms.Form):
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'ایمیل'
        }),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )

    password = forms.CharField(
        label='رمز عبور',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'رمز عبور'
        }),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )

    confirm_password = forms.CharField(
        label='تکرار رمز عبور',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'تکرار رمز عبور'
        })
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise ValidationError('کلمه عبور و تکرار آن یکسان نیست')

        return cleaned_data


class LoginForm(forms.Form):
    email= forms.EmailField(
        label= 'ایمیل',
        widget=forms.EmailInput(
            attrs={
                'class' :'form-control',
                'placeholder' : 'ایمیل'
            }
        ),
        validators= [
            validators.MaxLengthValidator(100),
            validators.EmailValidator,
        ]
    )
    password= forms.CharField(
        label='کلمه عبور',
        widget=forms.PasswordInput(
            attrs= {
                'class': 'form-control',
                'placeholder' : 'کلمه عبور'
            }
        ),
        validators= [validators.MaxLengthValidator(100),
            validators.EmailValidator,]
    )

class ResetPassword(forms.Form):
    email= forms.EmailField(
        label= 'ایمیل',
        widget=forms.EmailInput(
            attrs={
                'class' :'form-control',
                'placeholder' : 'ایمیل بازیابی'
            }
        ),
        validators= [
            validators.MaxLengthValidator(100),
            validators.EmailValidator,
        ]
    )

class ResetPassword(forms.Form):
    password = forms.CharField(
        label='تکرار کلمه عبور',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'تکرار کلمه عبور'
            }
        ),
        validators=[validators.MaxLengthValidator(100),
                    validators.EmailValidator, ]
    )
    confirm_password = forms.CharField(
        label='تکرار کلمه عبور',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'تکرار کلمه عبور'
            }

        ),
        validators=[
            validators.MaxLengthValidator(100),

        ]
    )

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get('new_password')
        confirm_new_password = cleaned_data.get('confirm_new_password')

        if new_password and confirm_new_password and new_password != confirm_new_password:
            raise ValidationError({
                'confirm_new_password': 'Passwords do not match'
            })
        return cleaned_data

class ForgetPassword(forms.Form):
    email = forms.EmailField(
        label= 'ایمیل',
        widget=forms.EmailInput(
            attrs={
               'class' : 'form-control',
                'placeholder' : 'ایمیل'
            }
        ),
        validators= [
            validators.MaxLengthValidator(100),
            validators.EmailValidator,
        ]
    )

class VerifyCodeForm(forms.Form):
    verification_code = forms.CharField(
        label='Verification Code',
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter verification code'
            }
        ),
        validators=[
            validators.MaxLengthValidator(100)
        ]
    )
