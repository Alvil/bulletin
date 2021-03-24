from django.views import generic
from django.urls import reverse_lazy

from .models import Article


class ArticleListView(generic.ListView):
    """
    List view for Article model
    Also serves as the landing page
    """
    model = Article
    template_name = 'article/index.html'


class ArticleDetailView(generic.DetailView):
    """
    Detail view for Article model
    """
    model = Article
    template_name = 'article/detail_view.html'


class ArticleCreateview(generic.CreateView):
    """
    Create view for Article model
    """
    model = Article
    template_name = 'article/create_view.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('article:list-view')


class ArticleUpdateView(generic.UpdateView):
    """
    Update view for Article model
    """
    model = Article
    template_name = 'article/update_view.html'


class ArticleDeleteView(generic.DeleteView):
    """
    Delete view for Article model
    """
    model = Article
    template_name = 'article/delete_view.html'
    success_url = reverse_lazy('article:list-view')
