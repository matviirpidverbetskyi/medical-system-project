from django import forms
from .models import Doctor

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['full_name', 'specialization', 'experience_years', 'bio', 'photo_url']

from django import forms
from .models import Doctor, Category, Service

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['category', 'name', 'price', 'is_available']