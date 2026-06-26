from django.db import models

# Create your models here.
class contact(models.Model):
    title = models.CharField(max_length=500 , verbose_name='موضوع تو')
    email = models.EmailField(max_length=500, verbose_name='ایمیل شما')
    name= models.CharField(max_length=500 , verbose_name= 'نام')
    # short_description = models.CharField(max_length=500 , null=True , db_index=True, verbose_name='توضیحات کوتاه')
    message = models.TextField( max_length=500 , verbose_name='پیغام تو')
    admin_message = models.TextField(verbose_name='پاسخ ادمین', null=True, blank=True)
    is_read_admin = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد پیام')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'تماس با ما '
        verbose_name_plural = 'لیست تماس با ما'