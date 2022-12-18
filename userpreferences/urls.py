from . import views
from django.urls import path

urlpatterns = [
    path('general/', views.general, name='general'),
    path('account/', views.account, name='account')
]
