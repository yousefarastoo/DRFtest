from django.shortcuts import render
from blog.models import Article
from .serializers import ArticleSerialiser
from rest_framework.generics import ListAPIView,ListCreateAPIView
# Create your views here.

class ArticleList(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerialiser


class ArticleCreateView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerialiser
