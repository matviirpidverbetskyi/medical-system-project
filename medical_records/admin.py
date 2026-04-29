from django.contrib import admin
from .models import Category, Service, Doctor

# Реєструємо моделі найпростішим способом
admin.site.register(Category)
admin.site.register(Service)
admin.site.register(Doctor)