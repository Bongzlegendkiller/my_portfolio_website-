from django.urls import path
from .import views


app_name='users'

urlpatterns=[
    path('', views.user_login, name='user_login'),
    path('user_create/', views.user_create, name='user_create'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('validate_user/', views.validate_user, name='validate_user')
]