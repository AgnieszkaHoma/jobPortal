from itertools import count
from turtle import title
from unicodedata import category
from django.test import TestCase, Client
from django.urls import reverse
from backend.models import Job, Application, Contact
import json

class TestViews(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.jobs_url = reverse('jobs')
            
    def test_jobs_GET(self):
        response = self.client.get(self.jobs_url)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'backend/jobs.html')
        