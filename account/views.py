from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import login, logout
from .models import Profile
import random
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def login_user(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('pass')
        print("Email:", email)  # Add debugging print statement
        print("Password:", password)  # Add debugging print statement
        
        user = auth.authenticate(username=email, password=password)
        print("User:", user)  # Add debugging print statement
        
        if user:
            try:
                prof = Profile.objects.get(user=user)
                if prof.is_verified:
                    login(request, user)
                    return redirect('hello')
                else:
                    messages.warning(request, 'Please verify your account')
            except Profile.DoesNotExist:
                messages.warning(request, 'Profile does not exist for this user')
        else:
            messages.warning(request, 'Invalid email or password')
    
    return render(request, 'account_template/login.html')



def registration_user(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('pass')
        password1 = request.POST.get('pass1')

        if password == password1:
            if User.objects.filter(username=email).exists():
                messages.warning(request, 'Account with this email already exist!')
                return redirect(registration_user)
            user = User.objects.create_user(username=email, email=email, password=password)
            user.set_password(password)
            user.save()

            otp = random.randint(0000,9999)

            prof = Profile(user=user, token = otp)
            prof.save()
            subject = 'OTP'
            message = f'Hi! here is your OTP = {otp}'
            from_email = settings.EMAIL_HOST_USER
            recipent = [email]
            send_mail(subject, message, from_email, recipent)
            messages.success(request, 'check email to verify successfully')
            return redirect('login_user')
        else:
            messages.warning(request, 'Not same password')

    return render(request, 'account_template/registration.html')

def logout_user(request):
    logout(request)
    messages.warning(request, 'User logged out')
    return redirect('login_user')

def verify_acc(request):
    if request.method == 'POST':
        otp = request.POST.get('otp')  # Corrected the variable name here
        try:
            prof = Profile.objects.get(token=otp)
            prof.is_verified = True
            prof.save()
            messages.success(request, 'Verify success!')
            return redirect('login_user')
        except Profile.DoesNotExist:
            messages.warning(request, 'Wrong OTP')
            return redirect('verify_acc')
    return render(request, 'account_template/Verify.html')