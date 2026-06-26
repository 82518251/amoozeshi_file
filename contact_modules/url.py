from django.urls import path
from . import views


urlpatterns =[
    path('', views.contact_fun_view.as_view() , name='contact_page')
]