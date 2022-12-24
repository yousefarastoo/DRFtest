from django.shortcuts import render
from .models import Article
# Create your views here.


def home(request):
    context = {"articles":Article.objects.filter(status=True)}
    return render(request, template_name="blog/index.html",context=context)