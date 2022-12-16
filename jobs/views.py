from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'jobs/index.html')

def show_jobs(request):
    return render(request, 'jobs/show_jobs.html')

def add_job(request):
    return render(request, 'jobs/add_job.html')