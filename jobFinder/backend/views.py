from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import *
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
import csv
from django.http import FileResponse
import io 
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator
# Create your views here.

def home(request):
    return render(request, 'backend/index.html')

class UserRegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'backend/register.html'
    success_url = reverse_lazy('loginPage')

def loginPage(request):
    
    page = 'loginPage'
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')
            
        user = authenticate(request, username=username, password=password)   
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password does not exist')
                       
    context = {'page': page}
    return render(request, 'backend/loginPage.html', context)

def signout(request):
    logout(request)
    return redirect('home')

def all_jobs(request):
    jobs = Job.objects.all()
    p = Paginator(Job.objects.all(), 3)
    page = request.GET.get('page')
    jobss = p.get_page(page)
    nums = "c" * jobss.paginator.num_pages
    return render(request, 'backend/jobs.html', {'jobs': jobs, 'jobss': jobss, 'nums':nums})
    

def about(request):   
    return render(request, 'backend/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'backend/message_send.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'backend/contact.html', context)

def job_info(request, job_id):
    job = Job.objects.get(pk=job_id)
    return render(request, 'backend/job_info.html', {'job': job})

class Search(ListView):
    model = Job
    template_name = 'backend/search.html'
    context_object_name = 'jobs'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Job.objects.filter(title__icontains=query).order_by('published')

# @login_required
# def delete_job(request, job_id):
#     job = Job.objects.get(pk=job_id)
#     if request.user == job.user:
#         Job.objects.filter(id=job_id).delete()
#         return redirect('backend/delete_job/<job_id>.html')


def signout(request):
    logout(request)
    return redirect('home')

@login_required
def board(request):
     return render(request, 'backend/board.html', {'useraccount': request.user.useraccount})

@login_required
def application(request, job_id):
    job = Job.objects.get(pk=job_id)

    if request.method == 'POST':
        form = ApplicationForm(request.POST)

        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.created_by = request.user
            application.save()
            
            return redirect('home')
    else:
        form = ApplicationForm()
    
    return render(request, 'backend/application.html', {'form': form, 'job': job})

@login_required
def profile(request, username):
    user = User.objects.get(username=username)
    return render(request, 'backend/profile.html', {"user" : user})

# class AddedJobsList(ListView):
#     model = Job
#     template_name = 'backend/added_jobs.html'
#     context_object_name = 'all_jobs'

#     def get_queryset(self):
#         return Job.objects.filter(user=self.request.user)
  
class AddJobView(LoginRequiredMixin, CreateView):
    model = Job
    template_name = 'backend/add_job.html'
    fields = '__all__'
    success_url = reverse_lazy('home')
    
class UserEditProfileView(LoginRequiredMixin, generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'backend/edit_profile.html'
    success_url = reverse_lazy('home')
    
    def get_object(self):
        return self.request.user
    
class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('home')

@login_required
def see_applications(request, application_id):
    application = get_object_or_404(Application, pk=application_id, created_by=request.user)
    
    return render(request, 'backend/see_applications.html', {'application': application})
