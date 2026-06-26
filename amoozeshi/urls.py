"""
URL configuration for amoozeshi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the index_modules() function: from django.urls import index_modules, path
    2. Add a URL to urlpatterns:  path('blog_modules/', index_modules('blog_modules.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index_modules.url')),
    path('product/', include('product_modules.url')),
    path('account/', include('account_modules.url')),
    path('contact/', include('contact_modules.url')),
    path('blog/', include('blog_modules.url')),
    path('teacher/', include('ins_modules.url')),
    path('order/', include('order_modules.url'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL , document_root =settings.MEDIA_ROOT)