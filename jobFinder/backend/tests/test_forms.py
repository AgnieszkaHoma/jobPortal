from django.test import SimpleTestCase
from backend.forms import ContactForm, NewJobForm, ApplicationForm

class TestForms(SimpleTestCase):
    
    def test_contact_form_valid_data(self):
        form = ContactForm(data={
            'email' : 'test@example.com',
            'title' : 'test title', 
            'message' : 'test message',
            
        })
        
        self.assertTrue(form.is_valid())
        
    def test_contact_form_no_data(self):
        form = ContactForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)
        
    
    def test_application_form_valid_data(self):
        form =  ApplicationForm(data={
            'fullName' : 'Marta Lis', 
            'email' : 'email@gmail.com', 
            'introduceYourself' : 'test introduceYourself',
            
        })
        
        self.assertTrue(form.is_valid())
        
    def test_application_form_no_data(self):
        form = ApplicationForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)
        
    def test_new_job_form_form_valid_data(self):
        form = NewJobForm(data={
            'title' : 'test title', 
            'company' : 'test company', 
            'jobType' : 'Full Time', 
            'category' : 'Backend', 
            'contractType' : 'B2B', 
            'experience' : 'Junior', 
            'description' : 'test description', 
            'proglanguage' : 'test proglanguage', 
            'place' : 'test place', 
            'salary' : '5000',
            
        })
    
        self.assertTrue(form.is_valid())
