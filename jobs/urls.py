from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('jobs-home/', views.jobs_home, name='jobs-home'),
    path('show-jobs/', views.show_jobs, name='show-jobs'),
    path('add-job/', views.add_job, name='add-jobs'),
    path('edit-job/<int:id>/', views.edit_job, name='edit-job'),
    path('delete-job/<int:id>/', views.delete_job, name='delete-job'),
]
