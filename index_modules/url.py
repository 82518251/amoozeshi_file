from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeView.as_view(), name='home_page'),
    path('about/', views.AboutView.as_view(), name='about_page' ),
    path('404/', views.not_fount_page, name='404_page'),
]