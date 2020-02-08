from django.shortcuts import render, get_object_or_404
from django.views import View
from django.urls import reverse
from .models import Article
#from .models import Course
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
    template_name = 'Blog/article_delete.html'

    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Article, id=id)
    
    def get_success_url(self):
        return reverse('Blog:article-list')

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

#----- function view coverting to classed based view ----------
#class CourseObjectMixin(object):
#   model = course
#   def get_object(self):
#       id = self.kwargs.get('id')
#       obj = None
#       if id is not None:
#           obj = get_object_or_404(self.model, id=id)
#       return obj
#
#class CourseDeleteView(CourseObjectMixin, View):
#   template_name = "courses/course_delete.html"
#   def get(self, request, id=None, *args, **kwargs):
#       context = {}
#       obj = sef.get_object()
#       if obj is not None:
#           context['object'] = obj
#       return render(request, self.template_name, context)
#
#   def post(self, request, id=None, *args, **kwargs):
#   #POST method
#       context = {}
#       obj = self.get_object()
#       if obj is not None:
#           obj.delete()
#           context['object'] = None
#           return redirect('/courses/')
#       return render(request, self.template_name, context)
#
#class CourseUpdateView(CourseObjectMixin, View):
#   template_name = 'courses/course_update.html"
#   def get(self, request, id=None, *args, **kwargs):
#   #GET method
#       context = {}
#       obj = self.get_object()
#       if obj is not None:
#           form = CourseModelForm(instance=obj)
#           context['object'] = obj
#           context['form'] = form
#       return render(request, self.template_name, context)
#
#   def post(self, request, id=None, *args, **kwargs):
#   #POST method
#       context = {}
#       obj = self.get_object()
#       if obj is not None:
#           form = CourseModelForm(request.POST, instance=obj)
#               if form.is_valid():
#                   form.save()
#               context['object'] = obj
#               context['form'] = form
#           return render(request, self.template_name, context)
#
#class CourseCreateView(CourseObjectMixinView):
#   template_name = "course/course_create.html"
#   def get(self, request, *args, **kwargs):
#       form = CourseModelForm()
#       context = {"form": form}
#       return render(request, self.template_name, context)
#   
#   def post(self, request, *args, **kwargs):
#       form = CourseModelForm(request.POST)
#       if form.is_valid():
#           form.save()
#           form = CourseModelForm()
#       context = {"form" : form}
#       return render(request, self.template_name, context)
#
#class CourseListView(View):
#   template_name = "courses/course_list.html"
#   queryset = Course.objects.all()
#
#   def get_queryset(self):
#       return self.queryset
#
#   def get(self, request, *args, **kwargs):
#       context = {'object_list': self.get_queryset()}
#       return render(request, self.template_name, context)
#
#class CourseDetailView(CourseObjectMixin, View):
#   template_name = 'courses/course_detail.html'
#   def get(self, request, id=None, *args, **kwargs):
#       context = {'object': self.get_object()}
#       return render(request, self.template_name, context)
#
# def my_fbv(request, *args, **kwargs):
#   print(request.method)
#   return render(request, 'about.html', {})

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