from django.db import models
from django.utils import timezone

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=120)
    date = models.DateField(default=timezone.now())
    abstract = models.CharField(max_length=500, default='')
    body = models.TextField(default='')