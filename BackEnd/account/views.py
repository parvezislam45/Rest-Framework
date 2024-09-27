from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib import messages

@login_required
def admin_dashboard(request):
    if not request.user.is_superuser:
        messages.error(request, 'You are not authorized to access this page.')
        return redirect('home')  # Redirect non-superusers to user dashboard
    return render(request, 'admin.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:  # Check if the user is an admin
                return redirect('admin')  # Redirect to admin dashboard
            else:
                return redirect('home')  # Redirect to user dashboard
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('home')  # Redirect back to login page
    else:
        return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

