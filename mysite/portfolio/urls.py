from django.urls import path
from .import views


app_name='portfolio'

urlpatterns=[
    path('', views.bongani_portfolio, name='bongani_portfolio')
    
]