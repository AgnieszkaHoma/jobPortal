from django.test import SimpleTestCase
from django.urls import reverse, resolve
from backend.views import *

class TestUrls(SimpleTestCase):
    
    def test_home_url_is_resolved(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home)
        
    def test_register_url_is_resolved(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func.view_class, UserRegisterView)  
        
    def test_login_url_is_resolved(self):
        url = reverse('loginPage')
        self.assertEquals(resolve(url).func, loginPage) 
        
    def test_jobs_url_is_resolved(self):
        url = reverse('jobs')
        self.assertEquals(resolve(url).func, all_jobs)
        
    def test_search_url_is_resolved(self):
        url = reverse('search')
        self.assertEquals(resolve(url).func.view_class, Search)
        
    def test_application_url_is_resolved(self):
        url = reverse('application', args=[2])
        self.assertEquals(resolve(url).func, application) 
        
    def test_profile_url_is_resolved(self):
        url = reverse('profile', args=['aga'])
        self.assertEquals(resolve(url).func, profile)
        
    def test_job_info_url_is_resolved(self):
        url = reverse('job_info', args=[1])
        self.assertEquals(resolve(url).func, job_info)
        
    def test_see_applications_url_is_resolved(self):
        url = reverse('see_applications', args=[3])
        self.assertEquals(resolve(url).func, see_applications)
    
    def test_delete_job_url_is_resolved(self):
        url = reverse('delete_job', args=[1])
        self.assertEquals(resolve(url).func.view_class, DeleteJobView)