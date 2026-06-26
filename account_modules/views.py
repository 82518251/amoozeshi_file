from django.shortcuts import render , redirect
from django.urls import reverse
from django.views import View
from .form import RegisterForm, ResetPassword,ForgetPassword ,LoginForm, VerifyCodeForm
from .models import User
from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string
from django.http import Http404, HttpRequest
from django.contrib.auth import login , logout
from django.core.mail import send_mail
from django.conf import settings
from utils.email_service import send_mail



class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'account_modules/register.page.html', {
            'register_form': register_form
        })

    def post(self, request):
        register_form = RegisterForm(request.POST)

        # print("VALID:", register_form.is_valid())
        # print("ERRORS:", register_form.errors)
        if register_form.is_valid():
            user_email = register_form.cleaned_data.get('email')
            user_password = register_form.cleaned_data.get('password')

            user_exists = User.objects.filter(email__iexact=user_email).exists()

            if user_exists:
                register_form.add_error('email', 'ایمیل وارد شده تکراری می باشد')
            else:
                new_user = User(
                    email=user_email,
                    email_active_code=get_random_string(72),
                    is_active=True,
                    username=user_email
                )

                new_user.set_password(user_password)
                new_user.save()

                return redirect(reverse('login_page'))

        return render(request, 'account_modules/register.page.html', {
            'register_form': register_form
        })



class LoginView(View):
    def get(self, request):
        login_form = LoginForm()
        context ={
            'login_form' : login_form
        }
        return render(request, 'account_modules/login.page.html', context)

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_email = login_form.cleaned_data.get('email')
            user_password = login_form.cleaned_data.get('password')
            user= User.objects.filter(email__exact=user_email).first()

            if user is not None:
                if not user.is_active:
                    login_form.add_error('email', 'حساب کاربری شما فعال نیست')
                else:
                    is_password_correct= user.check_password(user_password)
                    if is_password_correct:
                        login(request, user)
                        return redirect(reverse('home_page'))
                    else:
                        login_form.add_error('email', 'کلمه عبور شما اشتباهه')
            else:
                    login_form.add_error('email', 'کابری با مشخصات وارد شده یافت نشده است')
        context= {
            'login_form' : login_form
        }


        return  render(request, 'account_modules/login.page.html', context)

class ActiveAccountView(View):
    def get(self, request, email_active_code):
        User = User.objects.filter(email_active_code__iexact=email_active_code).first()
        if user is not None:
            if not user.is_active:
                user.is_active = True
                user.email_active_code = get_random_string(72)
                user.save()
                return redirect('login_page')
        else:
            pass
        Http404


class ForgetPasswordView(View):
    def get(self, request: HttpRequest):
        forget_form = ForgetPassword()
        return render(request, 'account_modules/forget.password.html', {
            'forget_form': forget_form
        })


    def post(self,request:HttpRequest):
            forget_form = ForgetPassword(request.POST)
            if forget_form.is_valid():
                user_email=forget_form.cleaned_data.get('email')
                user: User = User.objects.filter(email__iexact=user_email).first()
                if user is not None:
                    # send_email(
                    #     'تغییر کلمه عبور',
                    #     user_email,{'user':user},
                    #     'emails/forget.password.html'
                    # )
                    user.verification_code = get_random_string(20)
                    user.save()
                    return redirect(reverse('verify_page'))
                context= {
                    'forget_form' : forget_form
                }

                return render(request,'account_modules/forget.password.html', context)

class VerifyCodeView(View):
    def get(self,request:HttpRequest):
        verify_form = VerifyCodeForm()
        context = {
            'verify_form': verify_form
        }
        return render(request, 'account_modules/verify_code.html', context)



    def post(self, request:HttpRequest):
        verify_form = VerifyCodeForm(request.POST)
        if verify_form.is_valid():
            verification_code = verify_form.cleaned_data.get('verification_code')
            user : User = User.objects.filter(verification_code__iexact=verification_code).first()
            if user is not None:
                request.session['verification_code'] = verification_code
                return redirect(reverse('reset_page'))
            else:
                verify_form.add_error('verification_code', 'کد تایید نادرست است')
        context = {'verify_form': verify_form}
        return render(request, 'account_modules/verify_code.html', context)


class ResetPasswordView(View):
    def get(self, request: HttpRequest):
        verification_code = request.session.get('verification_code')
        if not verification_code:
            return redirect(reverse('forget_page'))

        reset_form = ResetPassword()
        context = {'reset_form': reset_form}
        return render(request, 'account_modules/reset.password.html', context)

    def post(self, request: HttpRequest):
        verification_code = request.session.get('verification_code')
        if not verification_code:
            return redirect(reverse('forget_page'))

        reset_form = ResetPassword(request.POST)
        if reset_form.is_valid():
            user: User = User.objects.filter(verification_code__iexact=verification_code).first()
            if user is not None:
                new_password = reset_form.cleaned_data.get('new_password')
                user.set_password(new_password)
                user.verification_code = ''
                user.save()
                # Clear session
                del request.session['verification_code']
                return redirect(reverse('index_page'))
            else:
                reset_form.add_error(None, 'خرابی در سیستم، لطفا دوباره تلاش کنید')
        context = {'reset_form': reset_form}
        return render(request, 'account_modules/reset.password.html', context)


# Create your views here.
