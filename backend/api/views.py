from django.shortcuts import render
from blog.models import Article
from .serializers import ArticleSerialiser
from rest_framework.generics import ListAPIView
# Create your views here.

class ArticleList(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerialiser
