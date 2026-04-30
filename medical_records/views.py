from django.shortcuts import render, get_object_or_404, redirect
from .models import Doctor
from .forms import DoctorForm , Category, CategoryForm

# 1. Створення лікаря
def doctor_form_view(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctor_list') # Повернемось до списку після збереження
    else:
        form = DoctorForm()
    
    context = {"title": "Додати лікаря", "form": form}
    return render(request, 'medical_records/doctor_form.html', context)

# 2. Список усіх лікарів
def doctor_list_view(request):
    doctors = Doctor.objects.all()
    context = {"title": "Наші спеціалісти", "doctors": doctors}
    return render(request, 'medical_records/doctor_list.html', context)

# 3. Детальна інформація про лікаря
def doctor_detail_view(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    context = {"title": f"Лікар: {doctor.full_name}", "doctor": doctor}
    return render(request, 'medical_records/doctor_detail.html', context)

# 4. Видалення лікаря
def doctor_delete_view(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    if request.method == 'POST':
        doctor.delete()
        return redirect('doctor_list')
    
    context = {"title": "Видалення профілю", "doctor": doctor}
    return render(request, 'medical_records/doctor_confirm_delete.html', context)

# --- VIEWS ДЛЯ SERVICE ---
def service_list_view(request):
    services = Service.objects.all()
    return render(request, 'medical_records/service_list.html', {'services': services, 'title': 'Медичні послуги'})

def service_form_view(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('service_list')
    else:
        form = ServiceForm()
    return render(request, 'medical_records/service_form.html', {'form': form, 'title': 'Додати послугу'})

def service_detail_view(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    return render(request, 'medical_records/service_detail.html', {'service': service})

def service_delete_view(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    if request.method == 'POST':
        service.delete()
        return redirect('service_list')
    return render(request, 'medical_records/service_confirm_delete.html', {'service': service})
# Заглушки для категорій, щоб сервер запустився
def category_list_view(request):
    categories = Category.objects.all()
    return render(request, 'medical_records/category_list.html', {'categories': categories, 'title': 'Список категорій'})

def category_form_view(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'medical_records/category_form.html', {'form': form, 'title': 'Додати категорію'})