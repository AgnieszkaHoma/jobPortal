from django.forms import ModelForm
from .models import *

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        
class NewJobForm(ModelForm):
    class Meta:
        model = Job 
        fields = ['title', 'company', 'jobType', 'category', 'contractType', 'experience', 'description', 'image', 'proglanguage', 'place', 'salary']
        
class ApplicationForm(ModelForm):
    class Meta:
        model = Application
        fields = ['fullName', 'email', 'introduceYourself', 'file']