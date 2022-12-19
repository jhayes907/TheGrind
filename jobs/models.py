from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.

class Job(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=now)
    title = models.TextField(max_length=30, default=None)
    location = models.CharField(max_length=20)
    salary = models.IntegerField(null=True, blank=True)
    stack = models.TextField(max_length=150)
    content = models.TextField(default=None)
    response = models.TextField(max_length=30)
    post_origin = models.CharField(max_length=20)
    category = models.CharField(max_length=255)
    
    def __str__(self):
        return self.category

    class Meta:
       ordering = ['-date']

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name