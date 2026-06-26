from django.urls import path
from . import views

urlpatterns=[
    path('', views.ArticleListView.as_view(), name= 'article_list'),
    path('cat/<str:category>' , views.ArticleDetailView.as_view(), name= 'article_by_category'),
    path ('<int:id>' , views.ArticleDetailView.as_view() , name = 'article_detail'),
]