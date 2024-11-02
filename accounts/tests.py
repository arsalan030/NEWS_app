from django.test import TestCase

# Create your tests here.
# accounts/tests.py
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

   
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

class SignupPageTests(TestCase):
    def test_signup_form(self):
        response = self.client.post(
            reverse("signup"),
            {
                "username": "testuser",
                "email": "testuser@email.com",
                "password1": "testpass123",
                "password2": "testpass123",
                "profession": "developer",
                "age" : "23",
            },
        )
        
        # Check if there are any form errors

        self.assertEqual(response.status_code, 302)  # Expected redirect after successful signup
        self.assertEqual(get_user_model().objects.count(), 1)  # Check if user was created
        user = get_user_model().objects.first()
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "testuser@email.com")
    def test_url_exists_at_correct_location_signupview(self):
        response = self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code, 200)
    def test_signup_view_name(self):
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
        "registration/signup.html")

   
    
   