from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import *
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request, 'backend/index.html')

def register(request):
    
    if request.method == "POST":
        username = request.POST['username']
        name = request.POST['name']
        surname = request.POST['surname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please, try some other username")
            return redirect('home')
            
        if User.objects.filter(email=email):
            messages.error(request, "Email already registered!")
            return redirect('home')
        
        if len(username)>15:
            messages.error(request, "Username must be under 15 characters")
            
        if password1 != password2:
            messages.error(request, "Passwords didn't match! Try again!")
            
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!")
            return redirect('home')
        
        myuser = User.objects.create_user(username, email, password1)
        myuser.first_name = name 
        myuser.last_name = surname
        myuser.is_active = False
        myuser.save() 
                  
        return redirect('loginPage')
    
    return render(request, "backend/register.html")

def loginPage(request):
    
    page = 'loginPage'
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == "POST":
        username = request.POST['username']
        password1 = request.POST['password1']
        
        user = authenticate(username=username, password=password1)
        
        if user is not None:
            login(request, user)
            name = user.first_name
            return render(request, 'backend/index.html', {'name': name})
            
        else:
            messages.error(request, "Bad Credentials!")
            return redirect('loginPage')
    
    context = {'page': page}
    return render(request, "backend/loginPage.html", context)

def signout(request):
    logout(request)
    return redirect('home')

def all_jobs(request):
    context = { 'jobs': Job.objects.all() }
    return render(request, 'backend/jobs.html', context)

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

@login_required
def add_job(request):
    if request.method == 'POST':
        form = NewJobForm(request.POST)

        if form.is_valid():
            job = form.save(commit=False)
            job.created_by = request.user
            job.save()
            messages.success(request, 'New job added!')

            return redirect('all_jobs')
    else:
        form = NewJobForm()
    
    return render(request, 'backend/add_job.html', {'form': form})

@login_required
def delete_job(request, id):
    job = get_object_or_404(Job, id=id, user=request.user.id)
    if job:
        job.delete()
        messages.success(request, 'Job offer was deleted!')

    return redirect('home')

def signout(request):
    logout(request)
    return redirect('home')

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
            
            return redirect('jobs')
    else:
        form = ApplicationForm()
    
    return render(request, 'backend/application.html', {'form': form, 'job': job})

@login_required
def profile(request, username):
    user = User.objects.get(username=username)
    return render(request, 'backend/profile.html', {"user" : user})