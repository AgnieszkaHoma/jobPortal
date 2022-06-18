import email
from django.test import TestCase
from backend.models import *

class TestModels(TestCase):
    
    def test_contact_model(self):
        email = Contact.objects.create(email= "aga@gmail.com")
        title = Contact.objects.create(title= "test")
        message = Contact.objects.create(message = "test message")
        date = Contact.objects.create(date = "2022-06-06")
        self.assertEqual(str(email), 'aga@gmail.com')
