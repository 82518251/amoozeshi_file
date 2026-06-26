from django.db import models
from django.urls import reverse
from account_modules.models import User


class ProductModel(models.Model):
    title= models.CharField(max_length=300, db_index=True, verbose_name='عنوان')
    url_title= models.CharField(max_length=300, db_index=True, verbose_name='عنوان در url')

    def __str__(self):
            return self.title

    class Meta :
        verbose_name= 'دسته بندی دوم'
        verbose_name_plural=  'دستبندی ها'


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='موضوع')
    slug = models.SlugField(unique=True, null=True)

    def __str__(self):
        return self.title



class Instructor(models.Model):
    full_name = models.CharField(max_length=200)
    position = models.CharField(max_length=100)

    image = models.ImageField(
        upload_to='instructors/'
    )

    description = models.TextField()


    def __str__(self):
        return self.full_name


    class Meta:
        verbose_name = 'مربی'
        verbose_name_plural = 'مربی ها'

class ProductTag(models.Model):
    caption= models.CharField(max_length=200, verbose_name='عنوان تگ')

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name= 'تگ'
        verbose_name_plural=  'تگ ها'

class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name='موضوع')
    category = models.ForeignKey(ProductModel, db_index=True, null=True, on_delete=models.CASCADE,verbose_name='دسته بندی دوره',
                                 related_name='product_model')
    # productBrand = models.ForeignKey(ProductBrand, db_index=True, on_delete=models.CASCADE, verbose_name='برند')
    productTag=models.ManyToManyField(ProductTag, verbose_name='تگ')

    price= models.IntegerField(default=0, verbose_name='قیمت')
    short_description = models.CharField(max_length=400, db_index=True, null=True,
                                         verbose_name='توضیحات کوتاه')
    description = models.TextField(null=True, verbose_name='توضیحات تکمیلی محصول')
    overview = models.TextField(blank=True,max_length=200, verbose_name='بررسی اجمالی')
    StudyPlan = models.TextField(null=True,verbose_name='برنامه تحصیلی')
    image = models.ImageField(upload_to='product/',max_length=300, default='', null=True, blank=True, db_index=True,
                              verbose_name=' تصویر ')
    instructor = models.ForeignKey(Instructor, on_delete=models.SET_NULL, null=True, blank=True)

    slug=models.SlugField(max_length=300 , db_index=True , verbose_name='عنوان در  url')
    is_active= models.BooleanField(default=True, verbose_name='فعال/غیرفعال')
    is_deleted= models.BooleanField(default=False, verbose_name='حذف/نشده')
    tool_dore= models.CharField(max_length=100,null=True, verbose_name='طول دوره')
    talk= models.IntegerField(null=True, blank=True, verbose_name='کل سخرانی ها')
    student = models.IntegerField(null=True, blank=True, verbose_name='کل دانش آموزان')
    madrak= models.CharField(max_length=100 ,default=0, verbose_name='گواهینامه')


    def get_absolute_url(self):
        return reverse('product_detail' , args=[self.slug])

    def __str__(self):
        return self.title

    class Meta:
        verbose_name= 'محصول'
        verbose_name_plural=  'محصول ها'


class ProductComment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    parent = models.ForeignKey('ProductComment', null=True, blank=True,
                               on_delete=models.CASCADE, related_name='parentcomment', verbose_name='والد')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='کالبد')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')
    text = models.TextField(verbose_name='متن نظر')
    name = models.CharField(max_length=100, null=True, blank=True, verbose_name='نام و نام خانوادگی')
    email = models.EmailField(null=True, blank=True, verbose_name='ایمیل')
    rating = models.PositiveSmallIntegerField(default=5)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='comments/', null=True, blank=True)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'نظر محصول'
        verbose_name_plural = 'نظرات محصول'





# Create your models here.

# Create your models here.
