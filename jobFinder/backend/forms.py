from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserChangeForm

class RegisterForm(UserCreationForm):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
class ContactForm(ModelForm):
    email = forms.EmailField(required=True)
    title = forms.CharField(max_length=500, required=True)
    message = forms.CharField(widget = forms.Textarea, max_length = 2000, required=True)
    class Meta:
        model = Contact
        fields = '__all__'
        
class NewJobForm(forms.ModelForm):
    class Meta:
        model = Job 
        fields = ['title', 'company', 'jobType', 'category', 'contractType', 'experience', 'description', 'proglanguage', 'place', 'salary']
class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['fullName', 'email', 'introduceYourself']
        
class EditProfileForm(UserChangeForm):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name','password')
     
