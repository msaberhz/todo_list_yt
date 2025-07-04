from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

from django.contrib.auth import logout
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login  # تغییر نام برای جلوگیری از تداخل




# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'the user already has an account')
                return redirect('sign_up')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'user has email')
                    return redirect('sign_up')
                else:
                    user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username, email=email, password=password)
                        
                    # حل مشکل چندین بک‌اند احراز هویت
                    user.backend = 'django.contrib.auth.backends.ModelBackend'
                    
                    # ورود کاربر به سیستم
                    auth_login(request, user)  # استفاده از نام مستعار
                    return redirect('home')
                    messages.success(request, 'you are success registered!')
                    return redirect('sign_up')
        else:
            messages.error(request, 'your password do not much!')
            return redirect('sign_up')
    else:
        return render(request, 'accounts/sign_up.html', )
    




def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'your logged in!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('sign_in')
    return render(request, 'accounts/sign_in.html')




def logout(request):
        auth.logout(request)
        messages.info(request, 'You are logged out successfully!')
        return redirect('sign_in')