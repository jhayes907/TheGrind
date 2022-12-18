from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request, 'index.html')

@login_required(login_url='/authentication/login')
def jobs_home(request):
    return render(request, 'jobs/jobs_home.html')

@login_required(login_url='/authentication/login')
def show_jobs(request):
    return render(request, 'jobs/show_jobs.html')

@login_required(login_url='/authentication/login')
def add_job(request):
    return render(request, 'jobs/add_job.html')