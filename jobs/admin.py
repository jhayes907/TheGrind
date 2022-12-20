from django.contrib import admin

# Register your models here.
from .models import JobPost, Category, Company, JobSite, Recruiter

admin.site.register(JobPost)
admin.site.register(Category)
admin.site.register(Company)
admin.site.register(JobSite)
admin.site.register(Recruiter)


