from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
# TODO: Set table relationships
class Category(models.Model):
    name = models.CharField(max_length=255)
    
    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Company(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    name = models.CharField(max_length=40, blank=False, unique=True)
    locations = models.CharField(max_length=50, blank=False)
    product = models.CharField(max_length=50, blank=False, unique=True)
    response = models.TextField(null=True, blank=True, max_length=40)

    class Meta:
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name


class JobPost(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=now)
    companyName = models.TextField(null=True, blank=False, max_length=30)
    title = models.TextField(max_length=30, default=None)
    locations = models.CharField(max_length=20)
    # salary = models.IntegerField(default=111, null=True)
    stack = models.CharField(max_length=150)
    content = models.URLField(default=None)
    post_origin = models.CharField(max_length=20)
    category = models.ManyToManyField(Category, blank=True)
    
    def __str__(self):
        return self.category

    class Meta:
       ordering = ['-date']





class JobSite(models.Model):
    name = models.CharField(max_length=20, unique=True)
    listings = models.ForeignKey(to=JobPost, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Recruiter(models.Model):
    name = models.CharField(max_length=30)
    listings = models.ForeignKey(to=JobPost, on_delete=models.CASCADE)
    response = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

# TODO: Model for Responses

# TODO: Model for Origin