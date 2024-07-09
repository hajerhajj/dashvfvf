# accounts/views.py
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from DashApp.models import OrAdmin
import os
from django.conf import settings
from .models import Int, Tn1MME,Tn2MME,SoMME
from django.http import JsonResponse
import schedule
import time



@login_required(login_url='login')
def HomePage(request):
    tn1_data = Tn1MME.objects.all()
    tn2_data = Tn2MME.objects.all()
    sousse_data = SoMME.objects.all()
    int_data = Int.objects.all()
    
    context = {
        'tn1_data': tn1_data,
        'tn2_data': tn2_data,
        'sousse_data': sousse_data,
        'int_data': int_data,
    }

    return render(request, 'index.html', context)
    response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'

    return response

from django.contrib import messages

def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            messages.error(request, "Your password and confirm password are not the same!!")
        else:
            if OrAdmin.objects.filter(email=email).exists():
                messages.error(request, "This email is already registered!")
            else:
                or_admin = OrAdmin(username=uname, email=email, password1=pass1, password2=pass2)
                or_admin.save()
                return redirect('login') 

    return render(request, 'signup.html', {})


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = OrAdmin.objects.get(username=username)
            if user.password1 == password:
                return redirect('index')
            else:
                messages.error(request, "Nom d'utilisateur ou mot de passe incorrect!")
                return render(request, 'login.html')
        except OrAdmin.DoesNotExist:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect!")
            return render(request, 'login.html')

    return render(request, 'login.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')

def HomePage(request):
    tn1_data = Tn1MME.objects.all()
    tn2_data = Tn2MME.objects.all()
    sousse_data = SoMME.objects.all()
    int_data = Int.objects.all()
    

    context = {
        'tn1_data': tn1_data,
        'tn2_data': tn2_data,
        'sousse_data': sousse_data,
        'int_data': int_data,

    }

    return render(request, 'index.html', context)

def readfiletn1(request):
    chemin_file = os.path.join(settings.BASE_DIR, 'static', 'files', 'resultmmetn1.txt')


    if os.path.isfile(chemin_file):
        with open(chemin_file, 'r') as f:
            for line in f:
                if line.strip():  # Ignore empty lines
                    data = line.strip().split('|')
                    if len(data) >= 8: 
                        try:
                            date_str = data[0].strip()
                            attach2g3g = float(data[1].strip())
                            attach4g = float(data[2].strip())
                            pdpact2g3g = float(data[3].strip())
                            attach3g = float(data[4].strip())
                            sau2g3g = int(float(data[5].strip()))
                            sau4g = int(float(data[6].strip()))
                            pdp = int(float(data[7].strip()))
                            bearer = int(float(data[8].strip()))

                            # Create or update instance of Tn1MME model
                            mm_instance, created = Tn1MME.objects.get_or_create(
                                date=date_str,
                                defaults={
                                    'attach2g3g': attach2g3g,
                                    'attach4g': attach4g,
                                    'pdpact2g3g': pdpact2g3g,
                                    'attach3g': attach3g,
                                    'sau2g3g': sau2g3g,
                                    'sau4g': sau4g,
                                    'pdp': pdp,
                                    'bearer': bearer,
                                }
                            )

                        except (ValueError, IndexError) as e:
                            continue

        return HttpResponse(f"Données du fichier importées dans la base PostgreSQL.")
    else:
        return HttpResponse(f"Fichier  non trouvé dans le répertoire spécifié.")
    

def readfiletn2(request):
    chemin_file = os.path.join(settings.BASE_DIR, 'static', 'files', 'resultmmetn2.txt')


    if os.path.isfile(chemin_file):
        with open(chemin_file, 'r') as f:
            for line in f:
                if line.strip():  # Ignore empty lines
                    data = line.strip().split('|')
                    if len(data) >= 8: 
                        try:
                            date_str = data[0].strip()
                            attach2g3g = float(data[1].strip())
                            attach4g = float(data[2].strip())
                            pdpact2g3g = float(data[3].strip())
                            attach3g = float(data[4].strip())
                            sau2g3g = int(float(data[5].strip()))
                            sau4g = int(float(data[6].strip()))
                            pdp = int(float(data[7].strip()))
                            bearer = int(float(data[8].strip()))

                            # Create or update instance of Tn1MME model
                            mm_instance, created = Tn2MME.objects.get_or_create(
                                date=date_str,
                                defaults={
                                    'attach2g3g': attach2g3g,
                                    'attach4g': attach4g,
                                    'pdpact2g3g': pdpact2g3g,
                                    'attach3g': attach3g,
                                    'sau2g3g': sau2g3g,
                                    'sau4g': sau4g,
                                    'pdp': pdp,
                                    'bearer': bearer,
                                }
                            )

                        except (ValueError, IndexError) as e:
                            continue

        return HttpResponse(f"Données du fichier importées dans la base PostgreSQL.")
    else:
        return HttpResponse(f"Fichier  non trouvé dans le répertoire spécifié.")

def readfileso(request):
    chemin_file = os.path.join(settings.BASE_DIR, 'static', 'files', 'resultmmeso.txt')


    if os.path.isfile(chemin_file):
        with open(chemin_file, 'r') as f:
            for line in f:
                if line.strip():  # Ignore empty lines
                    data = line.strip().split('|')
                    if len(data) >= 8: 
                        try:
                            date_str = data[0].strip()
                            attach2g3g = float(data[1].strip())
                            attach4g = float(data[2].strip())
                            pdpact2g3g = float(data[3].strip())
                            attach3g = float(data[4].strip())
                            sau2g3g = int(float(data[5].strip()))
                            sau4g = int(float(data[6].strip()))
                            pdp = int(float(data[7].strip()))
                            bearer = int(float(data[8].strip()))

                            # Create or update instance of Tn1MME model
                            mm_instance, created = SoMME.objects.get_or_create(
                                date=date_str,
                                defaults={
                                    'attach2g3g': attach2g3g,
                                    'attach4g': attach4g,
                                    'pdpact2g3g': pdpact2g3g,
                                    'attach3g': attach3g,
                                    'sau2g3g': sau2g3g,
                                    'sau4g': sau4g,
                                    'pdp': pdp,
                                    'bearer': bearer,
                                }
                            )

                        except (ValueError, IndexError) as e:
                            continue

        return HttpResponse(f"Données du fichier importées dans la base PostgreSQL.")
    else:
        return HttpResponse(f"Fichier  non trouvé dans le répertoire spécifié.")

def readfileint(request):
    chemin_file = os.path.join(settings.BASE_DIR, 'static', 'files', 'int.txt')


    if os.path.isfile(chemin_file):
        with open(chemin_file, 'r') as f:
            for line in f:
                if line.strip(): 
                    data = line.strip().split('|')
                    if len(data) >= 4: 
                        try:
                            date_str = data[0].strip()
                            bhTN1 = float(data[1].strip())
                            bhTN2 = float(data[2].strip())
                            bhSO = float(data[3].strip())
                            
                            mm_instance, created = Int.objects.get_or_create(
                                date=date_str,
                                defaults={
                                    'bhTN1': bhTN1,
                                    'bhTN2': bhTN2,
                                    'bhSO': bhSO,
                                    
                                }
                            )

                        except (ValueError, IndexError) as e:
                            # Handle errors if data format is incorrect
                            continue

        return HttpResponse(f"Données du fichier importées dans la base PostgreSQL.")
    else:
        return HttpResponse(f"Fichier  non trouvé dans le répertoire spécifié.")
    


