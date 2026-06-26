from django.db import models

class Teacher(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    name = models.CharField(max_length=200, verbose_name=' اسم مربی')
    slug = models.SlugField(max_length=300 ,default='' , null=True , blank=True , db_index=True , verbose_name='عنوان در  url')
    image = models.ImageField(upload_to='teacher/', verbose_name='تصویر')
    descreption = models.TextField(null=True,blank=True,verbose_name='توضیحات')
    gmail = models.URLField(blank=True,null=True,verbose_name="لینک جیمیل")
    phone_number = models.CharField(blank=True,null=True,verbose_name=" شماره تلفن")
    instagram = models.CharField(blank=True,null=True,verbose_name="لینک اینستاگرام")
    courses_count = models.PositiveIntegerField(default=0, verbose_name='دوره مربوطه')
    students_count = models.PositiveIntegerField(default=0, verbose_name='تعداد کارآموز')
    is_active = models.BooleanField(default=True, verbose_name='فعال/غیرفعال')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name= 'مربی'
        verbose_name_plural=  'مربی ها'

