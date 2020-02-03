from django.urls import path, include
from .views import (
    ArticleDetailView,
    ArticleListView,

)
#currently using class based views
#need to reimpliment 
#article_list_view as default home, detail view
#also need to import from .views function based view.py

app_name = 'Blog'
urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    path('<int:id>/', ArticleDetailView.as_view(), name='article-detail'), #cannot be str:title
]