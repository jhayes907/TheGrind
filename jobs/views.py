from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
from .models import Category, JobPost
from django.contrib import messages
from django.core.paginator import Paginator
import json
from django.http import JsonResponse
from . import models
# Create your views here.

@login_required(login_url='/authentication/login')
def home(request):
    return render(request, 'index.html')

@login_required(login_url='/authentication/login')
def jobs_home(request):
    categories = Category.objects.all()
    jobPosts = JobPost.objects.filter(owner=request.user)
    paginator = Paginator(jobPosts, 2)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)
    context = {
        'jobPosts': jobPosts,
        'page_obj': page_obj,
    }
    return render(request, 'jobs/jobs_home.html', context)

@login_required(login_url='/authentication/login')
def show_jobs(request):
    # categories = Category.objects.all()
    return render(request, 'jobs/show_jobs.html')

@login_required(login_url='/authentication/login')
def add_job(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'values': request.POST
    }
    if request.method == 'GET':
        return render(request, 'jobs/add_job.html', context)

    if request.method == 'POST':
        companyName=request.POST['companyName']
        title = request.POST['title']
        locations = request.POST['locations']
        salary = request.POST['salary']
        stack = request.POST['stack']
        post_origin = request.POST['post_origin']
        date = request.POST['date']
        category = request.POST['category']
        content = request.POST['content']
        
        if not companyName:
            messages.error(request, 'Please complete company field.')
            return render(request, 'jobs/add_job.html', context)

        if not title:
            messages.error(request, 'Please complete title field.')
            return render(request, 'jobs/add_job.html', context)
    
        if not locations:
            messages.error(request, 'Please complete locations field.')
            return render(request, 'jobs/add_job.html', context)

        if not salary:
            messages.error(request, 'Please complete salary field.')
            return render(request, 'jobs/add_job.html', context)

        if not stack:
            messages.error(request, 'Please complete stack field.')
            return render(request, 'jobs/add_job.html', context)

        if not post_origin:
            messages.error(request, 'Please complete post_origin field.')
            return render(request, 'jobs/add_job.html', context)

        if not date:
            messages.error(request, 'Please complete date field.')
            return render(request, 'jobs/add_job.html', context)

        if not category:
            messages.error(request, 'Please complete category field.')
            return render(request, 'jobs/add_job.html', context)

        if not content:
            messages.error(request, 'Please complete content field.')
            return render(request, 'jobs/add_job.html', context)


        JobPost.objects.create(owner=request.user, companyName=companyName, title=title, locations=locations, salary=salary, stack=stack, post_origin=post_origin, date=date, category=category, content=content)
        
        messages.success(request, "Job Post saved successfully!")
        return redirect('jobs-home')

def edit_job(request, id):
    jobPost = JobPost.objects.get(pk=id)
    categories = Category.objects.all()
    context = {
        'jobPost': jobPost,
        'values': jobPost,
        'categories': categories,
    }
    if request.method == 'GET':
        return render(request, 'jobs/edit_job.html', context)
    if request.method == 'POST': 
        companyName=request.POST['companyName']
        title = request.POST['title']
        locations = request.POST['locations']
        salary = request.POST['salary']
        stack = request.POST['stack']
        post_origin = request.POST['post_origin']
        date = request.POST['date']
        category = request.POST['category']
        content = request.POST['content']
        
        if not companyName:
            messages.error(request, 'Please complete company field.')
            return render(request, 'jobs/edit_job.html', context)

        if not title:
            messages.error(request, 'Please complete title field.')
            return render(request, 'jobs/edit_job.html', context)
    
        if not locations:
            messages.error(request, 'Please complete locations field.')
            return render(request, 'jobs/edit_job.html', context)

        if not salary:
            messages.error(request, 'Please complete salary field.')
            return render(request, 'jobs/edit_job.html', context)

        if not stack:
            messages.error(request, 'Please complete stack field.')
            return render(request, 'jobs/edit_job.html', context)

        if not post_origin:
            messages.error(request, 'Please complete post_origin field.')
            return render(request, 'jobs/edit_job.html', context)

        if not date:
            messages.error(request, 'Please complete date field.')
            return render(request, 'jobs/edit_job.html', context)

        if not category:
            messages.error(request, 'Please complete category field.')
            return render(request, 'jobs/edit_job.html', context)

        if not content:
            messages.error(request, 'Please complete content field.')
            return render(request, 'jobs/edit_job.html', context)


        jobPost.owner = request.user 
        jobPost.companyName = companyName 
        jobPost.title = title 
        jobPost.locations = locations 
        jobPost.salary = salary 
        jobPost.stack = stack 
        jobPost.post_origin = post_origin 
        jobPost.date = date 
        jobPost.category = category 
        jobPost.content = content

        jobPost.save()

        messages.success(request, "Job Post Updated successfully!")
        return redirect('jobs-home')



def delete_job(request, id):
    jobPost = JobPost.objects.get(pk=id)
    jobPost.delete()
    messages.success(request, "Job Post deleted")
    return redirect('jobs-home')


def search_jobs(request):
    if request.method == 'POST':


        search_str=json.loads(request.body).get('searchText')

        jobPosts=JobPost.objects.filter(
        companyName__icontains=search_str, owner=request.user) | JobPost.objects.filter(
        date__starts_with=search_str, owner=request.user) | JobPost.objects.filter(
        title__icontains=search_str, owner=request.user) | JobPost.objects.filter(
        locations__icontains=search_str, owner=request.user) | JobPost.objects.filter(
        salary__starts_with=search_str, owner=request.user) | JobPost.objects.filter(
        stack__icontains=search_str, owner=request.user) | JobPost.objects.filter(
        post_origin__starts_with=search_str, owner=request.user) | JobPost.objects.filter(
        category__icontains=search_str, owner=request.user)  

        data = jobPosts.values()

        return JsonResponse(list(data), safe=False)