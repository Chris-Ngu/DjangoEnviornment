from django.urls import path, include
from .views import (
    article_detail_view,
    article_list_view,

)

app_name = 'Blog'
urlpatterns = [
    path('', article_list_view, name='article-list'),
    path('<str:title>/', article_detail_view, name='article-detail'),
]