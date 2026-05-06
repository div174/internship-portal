from django.db import models
import uuid
import os

def rename_resume(instance, filename):
    ext = filename.split('.')[-1]
    # Secure random filename
    new_filename = f"{uuid.uuid4().hex}.{ext}"
    return os.path.join('resumes/', new_filename)

class Application(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Selected', 'Selected'),
        ('Rejected', 'Rejected'),
    ]

    full_name = models.CharField(max_length=255, verbose_name="Full Name")
    email = models.EmailField(verbose_name="Email Address")
    phone = models.CharField(max_length=20, verbose_name="Phone Number")
    college_name = models.CharField(max_length=255, verbose_name="College/University")
    skills = models.TextField(verbose_name="Skills")
    experience = models.TextField(blank=True, null=True, verbose_name="Experience")
    linkedin_url = models.URLField(blank=True, null=True, verbose_name="LinkedIn URL")
    resume = models.FileField(upload_to=rename_resume, verbose_name="Resume File")
    message = models.TextField(verbose_name="Why do you want to join?")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.full_name} - {self.status}"
