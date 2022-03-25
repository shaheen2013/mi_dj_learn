from django.shortcuts import render, redirect
from user.auth_forms import CustomAuthenticationForm, CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login as authLogin, logout as authLogout


# Create your views here.
def login(request):
    if request.user.is_authenticated:
        messages.add_message(request, messages.SUCCESS, 'You are already logged in!')
        return redirect('profile')

    form = CustomAuthenticationForm()
    if request.method == 'POST':
        form = CustomAuthenticationForm()
        uname = request.POST['username']
        upass = request.POST['password']
        user = authenticate(username=uname, password=upass)
        if user is None:
            messages.add_message(request, messages.ERROR, 'Username or password is incorrect!')
            return redirect('login')
        else:
            authLogin(request, user)
            messages.add_message(request, messages.SUCCESS, 'Logged in successful!')
            return redirect('profile')
    return render(request, 'login.html', {'title': 'User Login', 'form': form})


def register(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'User registered successfully.')
            return redirect('login')

    return render(request, 'register.html', {'title': 'User Registration', 'form': form})


def profile(request):
    return render(request, 'profile.html', {'title': 'User Dashboard'})


def logout(request):
    if request.user.is_authenticated:
        authLogout(request)
        messages.add_message(request, messages.SUCCESS, 'Logged out successful!')
    return redirect('login')
