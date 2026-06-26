from django.db import models
from account_modules.models import User
from product_modules.models import Product


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    is_paid = models.BooleanField(verbose_name='نهایی شده/نشده')
    pyment_date= models.DateField(verbose_name= 'تاریخ پرداخت', null=True, blank=True)

    def __str__(self):
        return str(self.id)


    class Meta :
        verbose_name =  'سبد خرید'
        verbose_name_plural =  'سبدهای  خرید کاربران'


class OrderDetail(models.Model):
    order = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orderdetails_set', verbose_name='سبد خرید')
    product = models.ForeignKey(Product , on_delete=models.CASCADE, verbose_name='محصول')
    final_price =  models.IntegerField(null=True, blank=True , verbose_name='قیمت نهایی تک محصول')
    count = models.IntegerField(verbose_name='تعداد')


    def __str__(self):
        return str(self.id)


        class Meta:
            verbose_name = 'جزِییات  سبد خرید'
            verbose_name_plural = 'لیست جزییات سبد خرید'

