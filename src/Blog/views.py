pfrom django.shortcuts import render, get_object_or_404
from .models import Article
from .forms import ArticleForm
from django.views.generic import(
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    ListView,
    DeleteView
)

#WIP, needs revision
class ArticleDeleteView(DeleteView):
    def get_object(self):
        id = self.kwargs.get("id")
        obj = get_object_or_404(Article, id=id)
        obj.delete()

class ArticleCreateView(CreateView):
    template_name = 'Blog/article_create.html'
    #model = Article
    form_class = ArticleForm
    queryset = Article.objects.all()

class ArticleDetailView(DetailView):
    #template_name = 'Blog/article_detail.html
    #queryset = Article.objects.all()
    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Article, id=id)

class ArticleListView(ListView):
    #template_name = 'Blog/article_list.html    This is to overwrite generic path
    queryset = Article.objects.all()            #Blog/<model>_list.html

#-------------- function based views below --------------------   
#   To reimplement, need to change the url paths
#def article_list_view(request):
#    queryset = Article.objects.all()
#    context = {
#     "object_list" : queryset
#    }
#    return render(request, "Blog/article_list.html", context)

#def article_detail_view(request, id):
#    obj = Article.objects.get(id=id)
#    context = {
#        'object': obj,
#    }
#    return render(request, "Blog/article_detail.html", context)