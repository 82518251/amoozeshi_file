from django.db import models
from django.urls import reverse


class index_page(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    title_url = models.CharField(max_length=200, verbose_name='عنوان در url')
    is_active = models.BooleanField(default=True, verbose_name='فعال/ غیرفعال')
    image= models.ImageField(max_length=300, default='',null=True , blank=True, db_index=True ,
                             verbose_name=' تصویر ')


    def __str__(self):
        return self.title
# Create your models here.
