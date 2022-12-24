from django.urls import path
from .views import ArticleList,ArticleCreateView

app_name="api"

urlpatterns = [
    path('', ArticleList.as_view(),name="list"),
    path('create', ArticleCreateView.as_view(),name="create"),
]
