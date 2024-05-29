from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from DashApp.models import OrAdmin

@login_required(login_url='login')
def HomePage(request):
    return render(request, 'index.html')

def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("Your password and confirm password are not the same!!")
        else:
            # Create and save a new OrAdmin instance
            or_admin = OrAdmin(username=uname, email=email, password1=pass1, password2=pass2)
            or_admin.save()
            return redirect('login')  # Redirect to login page after successful signup
    return render(request, 'signup.html')

def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return HttpResponse("Username or Password is incorrect!!!")
    return render(request, 'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')
