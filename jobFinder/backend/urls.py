from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('register',views.register, name="register"),
    path('loginPage',views.loginPage, name="loginPage"),
    path('signout',views.signout, name="signout"),
    path('jobs',views.all_jobs, name="jobs"),
    path('about',views.about, name="about"),
    path('contact',views.contact, name="contact"),
    path('jobs/<int:job_id>/', views.job_info, name='job_info'),
    path('search/', views.Search.as_view(), name='search'),
    path('add_job', views.add_job, name='add_job'),
]