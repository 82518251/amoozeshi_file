from django.urls import path
from . import  views

urlpatterns = [
     path('', views.TeacherListView.as_view(), name='teacher_list'),
     path('teacher<slug:slug>', views.TeacherDetailView.as_view(), name='teacher_detail')
 ]