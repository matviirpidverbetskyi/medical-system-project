from django.shortcuts import render, redirect
from .forms import UserRegistrationForm

def user_registration_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # Після реєстрації відправляємо на сторінку входу
            return redirect('login') 
    else:
        form = UserRegistrationForm()
    
    return render(request, 'users/register.html', {'form': form})