from tkinter import Place
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField


JOB_CHOICES = (
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time'), 
    ('Freelancer', 'Freelancer'),
)

CATEGORY_CHOICES = (
    ('Backend', 'Backend'),
    ('Frontend', 'Frontend'),
    ('Fullstack', 'Fullstack'),
    ('Web Developing', 'Web Developing'),
    ('Mobile', 'Mobile'),
    ('Testing', 'Testing'),
    ('Security', 'Security'),
    ('AI', 'AI'),
    ('Big Data', 'Big Data'),
    ('Game', 'Game'),
)

CONTRACT_CHOICES = (
    ('B2B', 'B2B'),
    ('Employment contract', 'Employment contract'),
    ('Contract of mandate', 'Contract of mandate'),
    ('Work contract', 'Work contract'),
    ('Internship', 'Internship'),
)

EXPERIENCE_CHOICES = (
    ('Trainee', 'Trainee'),
    ('Junior', 'Junior'),
    ('Mid', 'Mid'),
    ('Senior', 'Senior'),
    ('Expert', 'Expert'),
)   
 
class Contact(models.Model):
    email = models.EmailField(null=True, blank=True)
    title = models.CharField(max_length=500, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.email
    
class Job(models.Model):
    user = models.ForeignKey(User, related_name='useraccount', on_delete=models.CASCADE, null=True, blank=True, editable=False)
    title = models.CharField(max_length=200, null=True, blank=True)
    company = models.CharField(max_length=200, null=True, blank=True)
    jobType = models.CharField(choices=JOB_CHOICES, max_length = 50, null=True, blank=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length = 50, null=True, blank=True)
    contractType = models.CharField(choices=CONTRACT_CHOICES, max_length = 50, null=True, blank=True)
    experience = models.CharField(choices=EXPERIENCE_CHOICES, max_length = 50, null=True, blank=True)
    description = RichTextField(blank=True, null=True)
    language =  models.CharField(max_length=200, null=True, blank=True)
    place = models.CharField(max_length=200, null=True, blank=True)
    salary = models.CharField(max_length=200, null=True, blank=True)
    published = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-published']
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('job_info', args=(str(self.id)))
    
class Application(models.Model):
    job = models.ForeignKey(Job, related_name='applications', on_delete=models.CASCADE, null=True)
    fullName = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField()   
    introduceYourself = models.TextField(null=True)
    file = models.FileField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    created_by = models.ForeignKey(User, related_name='applications', on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.fullName