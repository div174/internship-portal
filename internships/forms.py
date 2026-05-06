from django import forms
from django.core.exceptions import ValidationError
from .models import Application
import os

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = [
            'full_name', 'email', 'phone', 'college_name', 
            'skills', 'experience', 'linkedin_url', 'resume', 'message'
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Jane Doe'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'jane@example.com'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+1 234 567 8900'}),
            'college_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'University Name'}),
            'skills': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'e.g., Python, Django, React, Communication...'}),
            'experience': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Briefly describe your relevant experience (if any)'}),
            'linkedin_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://linkedin.com/in/username'}),
            'resume': forms.FileInput(attrs={'class': 'form-control', 'accept': '.pdf,.doc,.docx'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Tell us why you are a good fit for Amaanitvam...'}),
        }

    def clean_resume(self):
        resume = self.cleaned_data.get('resume')
        if resume:
            # Check file extension
            ext = os.path.splitext(resume.name)[1].lower()
            valid_extensions = ['.pdf', '.doc', '.docx']
            if ext not in valid_extensions:
                raise ValidationError("Only PDF, DOC, and DOCX files are allowed.")
            
            # Check file size (e.g., max 5MB)
            max_size = 5 * 1024 * 1024 # 5 MB
            if resume.size > max_size:
                raise ValidationError("Resume file size cannot exceed 5MB.")
                
        return resume
