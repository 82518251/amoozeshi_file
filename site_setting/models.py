from django.db import models

class SiteSetting(models.Model):
    site_name= models.CharField(max_length=200, verbose_name='نام سایت')
    site_url = models.CharField(max_length=200, verbose_name='دامنه سایت')
    address = models.TextField(max_length=200, verbose_name='آدرس')
    phone = models.CharField(max_length=200, verbose_name='تلفن')
    fax = models.CharField(max_length=200, verbose_name='فکس')
    email = models.EmailField(max_length=200, verbose_name='ایمیل')
    copy_right = models.CharField(max_length=300, verbose_name='متن کپی رایت')
    about_us_text = models.TextField(max_length=500, verbose_name='متن درباره ما سایت')
    site_logo = models.ImageField(upload_to='site_setting/', verbose_name='لوگو سایت')
    is_main_setting = models.BooleanField( verbose_name='تنظیمات اصلی')

    def __str__(self):
        return self.site_name

    class Meta:
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural = 'تنظیمات'

class FooterLinkBox(models.Model):
    title = models.CharField(max_length=200 , verbose_name='عنوان')

    class Meta:
        verbose_name = 'دسته بندی لینک های فوتر'
        verbose_name_plural =  ' دسته بندی های لینک های فوتر'

    def __str__(self):
        return self.title

class FooterLink(models.Model):
    title = models.CharField(max_length=200 , verbose_name='عنوان')
    url= models.URLField(max_length=200, verbose_name='لینک')
    footer_link_box = models.ForeignKey(to=FooterLinkBox ,
                                        on_delete=models.CASCADE, verbose_name='ذستع بندی')

    class Meta :
        verbose_name = 'لینک فوتر'
        verbose_name_plural = 'لینک های فوتر'

    def __str__(self):
            return self.title

class Slider(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    url = models.URLField(max_length=200, verbose_name='لینک')
    url_title =  models.CharField(max_length=200 , verbose_name= 'عنوان لینک')
    description = models.TextField(verbose_name= 'توضیحات اسلایدر')
    image = models.ImageField(upload_to='slider/', verbose_name= 'تصویر اسلایدر')
    is_active = models.BooleanField(default=True, verbose_name= 'فعال / غیرقعال ')

    class Meta:
        verbose_name = 'اسلایدر'
        verbose_name_plural = 'اسلایدرها'

        def __str__(self):
            return self.title
# Create your models here.
