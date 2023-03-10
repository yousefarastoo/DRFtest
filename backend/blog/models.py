from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField()
    status = models.BooleanField(default=False)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    