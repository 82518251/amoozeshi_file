from django.db import models


from django.db import models
from account_modules.models import User

from  django.urls import reverse
# Create your models here.

class ArticlaCategory(models.Model):
    parent= models.ForeignKey('ArticlaCategory', null=True, blank=True,
                              on_delete=models.CASCADE, verbose_name='دسته بندی والد')
    title = models.CharField(max_length=200, verbose_name='عنوان دسته بندی')
    url_title = models.CharField(max_length=200, unique=True, verbose_name='عنوان در url')
    is_active = models.BooleanField(default=True, verbose_name='فعال/ غیرفعال')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی مقاله'
        verbose_name_plural = 'دسته بندی های مقاله'

class Article(models.Model):
        title= models.CharField(max_length=300, verbose_name='عنوان مقاله')
        slug= models.SlugField(max_length=400, db_index=True, allow_unicode=True,
                               verbose_name='عنوان در url')
        image= models.ImageField(upload_to='article/', verbose_name='تصویر مقاله')
        short_description= models.TextField(verbose_name='توضیحات کوتاه')
        Text = models.TextField(verbose_name='متن مقاله')
        is_Active= models.BooleanField(default=True, verbose_name='فعال/ غیرفعال')
        selected_categoris= models.ManyToManyField(ArticlaCategory, verbose_name='دسته بندی مقاله')
        author = models.ForeignKey(User,on_delete=models.CASCADE , verbose_name= 'نویسنده ',
                                   null=True, editable=False )
        create_date= models.DateTimeField(auto_now_add=True , editable=False,
                                          verbose_name='تاریخ ثبت')

        def get_absolute_url(self):
            return reverse('article_detail', args=[self.id])

        def __str__(self):
            return self.title

        class Meta :
            verbose_name =' مقاله'
            verbose_name_plural= 'مقالات'

class Newsletter(models.Model):
    email = models.EmailField(unique=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class ArticleComment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='مقاله')
    parent = models.ForeignKey('ArticleComment' , null=True, blank=True,
                               on_delete=models.CASCADE, related_name='articlecomment_set' , verbose_name='والد')
    user = models.ForeignKey(User, on_delete=models.CASCADE , null=True, blank=True,
                             verbose_name='کاربر')
    create_date= models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')
    text= models.CharField(verbose_name='موضوع نظر', max_length=200)
    description= models.TextField(null=True , verbose_name='توضیحات ')
    name= models.CharField(max_length=100 , null=True, blank=True,
                           verbose_name='نام و نام خانوادگی')
    email= models.EmailField(null=True, blank=True, verbose_name='ایمیل')
    image = models.ImageField(upload_to='comments/', null=True, blank=True)
    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = ' نظر مقاله'
        verbose_name_plural = 'نظر مقالات'


# Create your models here.
