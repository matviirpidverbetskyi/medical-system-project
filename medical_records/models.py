from django.db import models

# 1. Модель Category (в нашому випадку - Спеціалізація/Відділення)
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва відділення")
    description = models.TextField(blank=True, null=True, verbose_name="Опис відділення")

    def __str__(self):
        return self.name

# 2. Модель Product (в нашому випадку - Медична послуга)
class Service(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='services')
    name = models.CharField(max_length=200, verbose_name="Назва послуги")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Вартість")
    is_available = models.BooleanField(default=True, verbose_name="Доступна для запису")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата додавання")

    def __str__(self):
        return self.name

# 3. Твоя власна модель - Doctor (Лікар)
class Doctor(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="ПІБ Лікаря")
    specialization = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    experience_years = models.PositiveIntegerField(verbose_name="Стаж роботи (років)")
    bio = models.TextField(verbose_name="Коротка біографія")
    photo_url = models.URLField(blank=True, verbose_name="Посилання на фото")

    def __str__(self):
        return f"{self.full_name} ({self.specialization.name if self.specialization else 'Не вказано'})"