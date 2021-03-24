from django.urls import path

from .views import ArticleDetailView
from .views import ArticleListView
from .views import ArticleCreateview
from .views import ArticleUpdateView
from .views import ArticleDeleteView

app_name = "article"

urlpatterns = [
    path('', ArticleListView.as_view(), name='list-view'),
    path('create/', ArticleCreateview.as_view(), name='create-view'),
    path('<pk>/', ArticleDetailView.as_view(), name='detail-view'),
    path('<pk>/update/', ArticleUpdateView.as_view(), name='update-view'),
    path('<pk>/delete/', ArticleDeleteView.as_view(), name='delete-view'),
    ]
