from django.urls import path, include
from .views import (
    ArticleDetailView,
    ArticleListView,
    ArticleCreateView,
    ArticleDeleteView,

)
#currently using class based views
#need to reimpliment 
#article_list_view as default home, detail view, createview
#also need to import from .views function based view.py

app_name = 'Blog'
urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    path('<int:id>/', ArticleDetailView.as_view(), name='article-detail'),
    path('create/', ArticleCreateView.as_view(), name='aricle-list'),
    path('<int:id>/delete/', ArticleDeleteView.as_view(), name='article-delete'),

]