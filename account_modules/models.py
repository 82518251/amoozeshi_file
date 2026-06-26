from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser


class User(AbstractUser):
    avatar= models.CharField(max_length=20, verbose_name='تصویر آواتار',null=True,
                             blank=True)
    email_active_code= models.CharField(max_length=100,verbose_name='کد فعال سازی ایمیل')
    phone_number= models.CharField(max_length=200, verbose_name='تلفن همراه')
    about_user= models.TextField(max_length=500, null=True ,blank=True , verbose_name='درباره من')
    address= models.TextField(null=True, blank=True, verbose_name='آدرس')

    class Meta:
        verbose_name= 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        if self.first_name is not '' and self.last_name is not '':
            return self.get_full_name()


        return self.email
# Create your models here.
