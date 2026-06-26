from django.contrib import admin
from . import models

admin.site.register(models.Article)
admin.site.register(models.ArticlaCategory)
admin.site.register(models.ArticleComment)
# Register your models here.
