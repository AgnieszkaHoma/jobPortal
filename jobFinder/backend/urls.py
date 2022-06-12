from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from . views import AddJobView, UserEditProfileView, PasswordsChangeView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('register',views.UserRegisterView.as_view(), name="register"),
    path('loginPage',views.loginPage, name="loginPage"),
    path('signout',views.signout, name="signout"),
    path('jobs',views.all_jobs, name="jobs"),
    path('about',views.about, name="about"),
    path('contact',views.contact, name="contact"),
    path('jobs/<int:job_id>/', views.job_info, name='job_info'),
    path('search/', views.Search.as_view(), name='search'),
    path('add_job', AddJobView.as_view(), name='add_job'),
    path('jobs/<int:job_id>/application/', views.application, name='application'),
    path('profile/<username>/', views.profile, name='profile'),
    path('edit_profile', UserEditProfileView.as_view(), name='edit_profile'),
    path('password', PasswordsChangeView.as_view(template_name='backend/change_password.html'), name = 'change_password'),
    path('<int:job_id>/application/', views.application, name = 'application'),
    path('board', views.board, name='board'),
    path('application/<int:application_id>', views.see_applications, name='see_applications'),
    path('job/<pk>/delete_job', views.DeleteJobView.as_view(), name='delete_job'),
    path('contact_list', views.contact_list, name='contact_list'),
    ]