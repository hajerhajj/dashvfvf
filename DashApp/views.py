# accounts/views.py
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from DashApp.models import OrAdmin
import os
from django.conf import settings
from .models import Int, Tn1EPG, Tn1MME,Tn2MME,SoMME , SOEPG, TN2VEPG
from django.http import JsonResponse

@login_required(login_url='login')
def HomePage(request):
    tn1_data = Tn1MME.objects.all()
    tn2_data = Tn2MME.objects.all()
    sousse_data = SoMME.objects.all()
    tn1global_data = Tn1MME.objects.all()
    tn2global_data = Tn2MME.objects.all()
    sousseglobal_data = SoMME.objects.all()
    int_data = Int.objects.all()
    tn1epg_data = Tn1EPG.objects.all()
    tn2vepg_data = TN2VEPG.objects.all()
    soepg_data = SOEPG.objects.all()
    
    context = {
        'tn1_data': tn1_data,
        'tn2_data': tn2_data,
        'sousse_data': sousse_data,
        'tn1global_data': tn1global_data,
        'tn2global_data': tn2global_data,
        'sousseglobal_data': sousseglobal_data,
        'int_data': int_data,
        'tn1epg_data': tn1epg_data,
        'tn2vepg_data': tn2vepg_data,
        'soepg_data': soepg_data,

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
    tn1global_data = Tn1MME.objects.all()
    tn2global_data = Tn2MME.objects.all()
    sousseglobal_data = SoMME.objects.all()
    int_data = Int.objects.all()
    tn1epg_data = Tn1EPG.objects.all()
    tn2vepg_data = TN2VEPG.objects.all()
    soepg_data = SOEPG.objects.all()
    
    context = {
        'tn1_data': tn1_data,
        'tn2_data': tn2_data,
        'sousse_data': sousse_data,
        'tn1global_data': tn1global_data,
        'tn2global_data': tn2global_data,
        'sousseglobal_data': sousseglobal_data,
        'int_data': int_data,
        'tn1epg_data': tn1epg_data,
        'tn2vepg_data': tn2vepg_data,
        'soepg_data': soepg_data,

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
                            pdpactnbr2g = int(float(data[9].strip()))
                            pdpactnbr3g = int(float(data[10].strip()))

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
                                    'pdpactnbr2g': pdpactnbr2g,
                                    'pdpactnbr3g': pdpactnbr3g,
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
                            pdpactnbr2g = int(float(data[9].strip()))
                            pdpactnbr3g = int(float(data[10].strip()))

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
                                    'pdpactnbr2g': pdpactnbr2g,
                                    'pdpactnbr3g': pdpactnbr3g,
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
                            pdpactnbr2g = int(float(data[9].strip()))
                            pdpactnbr3g = int(float(data[10].strip()))

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
                                    'pdpactnbr2g': pdpactnbr2g,
                                    'pdpactnbr3g': pdpactnbr3g,
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
                            continue

        return HttpResponse(f"Données du fichier importées dans la base PostgreSQL.")
    else:
        return HttpResponse(f"Fichier  non trouvé dans le répertoire spécifié.")


def readfiletn1epg(request):
    chemin_file = os.path.join(settings.BASE_DIR, 'static', 'files', 'max_output_filetn1.txt')


    if os.path.isfile(chemin_file):
        with open(chemin_file, 'r') as f:
            for line in f:
                if line.strip(): 
                    data = line.strip().split('|')
                    if len(data) >= 4: 
                        try:
                            date_str = data[0].strip()
                            avg16 = int(data[1].strip())
                            peak16 = int(data[2].strip())
                            avg4 = int(data[3].strip())
                            peak4 = int(data[4].strip())
                            avg5 =int(data[5].strip())
                            peak5 = int(data[6].strip())
                            avg14 = int(data[7].strip())
                            peak14 = int(data[8].strip())
                            avg15 = int(data[9].strip())
                            peak15 = int(data[10].strip())
                            avg17 = int(data[11].strip())
                            peak17 = int(data[12].strip())
                            avg6 = int(data[13].strip())
                            peak6 = int(data[14].strip())
                            actpdpcont = int(data[15].strip())
                            acteps = int(data[16].strip())
                            actsub = int(data[17].strip())
                            
                            mm_instance, created = Tn1EPG.objects.get_or_create(
                                date=date_str,
                                defaults={
                                    'avg16': avg16,
                                    'peak16': peak16,
                                    'avg4': avg4,
                                    'peak4': peak4,
                                    'avg5': avg5,
                                    'peak5': peak5,
                                    'avg14': avg14,
                                    'peak14': peak14,
                                    'avg15': avg15,
                                    'peak15': peak15,
                                    'avg17': avg17,
                                    'peak17': peak17,
                                    'avg6': avg6,
                                    'peak6': peak6,
                                    'actpdpcont': actpdpcont,
                                    'acteps': acteps,
                                    'actsub': actsub,
                                    
                                }
                            )

                        except (ValueError, IndexError) as e:
                            # Handle errors if data format is incorrect
                            continue

        return HttpResponse(f"Données du fichier importées dans la base PostgreSQL.")
    else:
        return HttpResponse(f"Fichier  non trouvé dans le répertoire spécifié.")
    
def readfilesoepg(request):
    chemin_file = os.path.join(settings.BASE_DIR, 'static', 'files', 'max_output_fileso.txt')


    if os.path.isfile(chemin_file):
        with open(chemin_file, 'r') as f:
            for line in f:
                if line.strip(): 
                    data = line.strip().split('|')
                    if len(data) >= 4: 
                        try:
                            date_str = data[0].strip()
                            avg29 = int(data[1].strip())
                            peak29 = int(data[2].strip())
                            avg30 = int(data[3].strip())
                            peak30 = int(data[4].strip())
                            avg1 =int(data[5].strip())
                            peak1 = int(data[6].strip())
                            avg2 = int(data[7].strip())
                            peak2 = int(data[8].strip())
                            avg3 = int(data[9].strip())
                            peak3 = int(data[10].strip())
                            avg4 = int(data[11].strip())
                            peak4 = int(data[12].strip())
                            avg5 = int(data[13].strip())
                            peak5 = int(data[14].strip())
                            avg6 = int(data[15].strip())
                            peak6 = int(data[16].strip())
                            actpdpcont = int(data[17].strip())
                            acteps = int(data[18].strip())
                            actsub = int(data[19].strip())
                            
                            mm_instance, created = SOEPG.objects.get_or_create(
                                date=date_str,
                                defaults={
                                    'avg29':avg29,
                                    'peak29':peak29,
                                    'avg30':avg30,
                                    'peak30':peak30,
                                    'avg1':avg1,
                                    'peak1':peak1,
                                    'avg2':avg2,
                                    'peak2':peak2,
                                    'avg3':avg3,
                                    'peak3':peak3,
                                    'avg4': avg4,
                                    'peak4': peak4,
                                    'avg5': avg5,
                                    'peak5': peak5,
                                    'avg6': avg6,
                                    'peak6': peak6,
                                    'actpdpcont': actpdpcont,
                                    'acteps': acteps,
                                    'actsub': actsub,
                                    
                                }
                            )

                        except (ValueError, IndexError) as e:
                            # Handle errors if data format is incorrect
                            continue

        return HttpResponse(f"Données du fichier importées dans la base PostgreSQL.")
    else:
        return HttpResponse(f"Fichier  non trouvé dans le répertoire spécifié.")
    

def readfiletn2epg(request):
    chemin_file = os.path.join(settings.BASE_DIR, 'static', 'files', 'max_output_filetn2vepg.txt')


    if os.path.isfile(chemin_file):
        with open(chemin_file, 'r') as f:
            for line in f:
                if line.strip(): 
                    data = line.strip().split('|')
                    if len(data) >= 4: 
                        try:
                            date_str = data[0].strip()
                            avg29 = int(data[1].strip())
                            peak29 = int(data[2].strip())
                            avg30 = int(data[3].strip())
                            peak30 = int(data[4].strip())
                            avg1 =int(data[5].strip())
                            peak1 = int(data[6].strip())
                            avg10 = int(data[7].strip())
                            peak10 = int(data[8].strip())
                            avg11 = int(data[9].strip())
                            peak11 = int(data[10].strip())
                            avg12 = int(data[11].strip())
                            peak12 = int(data[12].strip())
                            avg2 = int(data[13].strip())
                            peak2 = int(data[14].strip())
                            avg3 = int(data[15].strip())
                            peak3 = int(data[16].strip())
                            avg4 = int(data[17].strip())
                            peak4 = int(data[18].strip())
                            avg5 = int(data[19].strip())
                            peak5 = int(data[20].strip())
                            avg6 = int(data[21].strip())
                            peak6 = int(data[22].strip())
                            avg7 = int(data[23].strip())
                            peak7 = int(data[24].strip())
                            avg8 = int(data[25].strip())
                            peak8 = int(data[26].strip())
                            avg9 = int(data[27].strip())
                            peak9 = int(data[28].strip())
                            actpdpcont = int(data[29].strip())
                            acteps = int(data[30].strip())
                            actsub = int(data[31].strip())
                            
                            mm_instance, created = TN2VEPG.objects.get_or_create(
                                date=date_str,
                                defaults={
                                    'avg29': avg29,
                                    'peak29': peak29,
                                    'avg30': avg30,
                                    'peak30': peak30,
                                    'avg1': avg1,
                                    'peak1': peak1,
                                    'avg10': avg10,
                                    'peak10': peak10,
                                    'avg11': avg11,
                                    'peak11': peak11,
                                    'avg12': avg12,
                                    'peak12': peak12,
                                    'avg2': avg2,
                                    'peak2': peak2,
                                    'avg3': avg3,
                                    'peak3': peak3,
                                    'avg4': avg4,
                                    'peak4': peak4,
                                    'avg5': avg5,
                                    'peak5': peak5,
                                    'avg6': avg6,
                                    'peak6': peak6,
                                    'avg7': avg7,
                                    'peak7': peak7,
                                    'avg8': avg8,
                                    'peak8': peak8,
                                    'avg9': avg9,
                                    'peak9': peak9,
                                    'actpdpcont': actpdpcont,
                                    'acteps': acteps,
                                    'actsub': actsub,
                                    
                                }
                            )

                        except (ValueError, IndexError) as e:
                            # Handle errors if data format is incorrect
                            continue

        return HttpResponse(f"Données du fichier importées dans la base PostgreSQL.")
    else:
        return HttpResponse(f"Fichier  non trouvé dans le répertoire spécifié.")
    

from django.shortcuts import render

def mme_view(request):
    tn1_data = Tn1MME.objects.all()
    tn2_data = Tn2MME.objects.all()
    sousse_data = SoMME.objects.all()
    
    
    context = {
        'tn1_data': tn1_data,
        'tn2_data': tn2_data,
        'sousse_data': sousse_data,
    }
    return render(request, 'MMEomea.html',context)

def int_view(request):
    int_data = Int.objects.all()
    
    context = {
        'int_data': int_data,
        
    }
    return render(request, 'MMEint.html',context)

def global_view(request):
    tn1global_data = Tn1MME.objects.all()
    tn2global_data = Tn2MME.objects.all()
    sousseglobal_data = SoMME.objects.all()
    
    
    context = {
        
        'tn1global_data': tn1global_data,
        'tn2global_data': tn2global_data,
        'sousseglobal_data': sousseglobal_data,
        
    }
    return render(request, 'MMEglobal.html',context)

def epg_view(request):
    tn1epg_data = Tn1EPG.objects.all()
    tn2vepg_data = TN2VEPG.objects.all()
    soepg_data = SOEPG.objects.all()
    
    context = {
        'tn1epg_data': tn1epg_data,
        'tn2vepg_data': tn2vepg_data,
        'soepg_data': soepg_data,

    }
    return render(request, 'epg.html',context)
