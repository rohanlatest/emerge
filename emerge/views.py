from django.contrib import auth, messages
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect


def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            return redirect('udashboard')
        #    auth.login(request, user)
        #    if request.user.is_loginuser:
        #        return redirect('udashboard')
        #    elif request.user.is_manager:
        #        return redirect('mdashboard')
        #    elif request.user.is_admin:
        #        return redirect('dashboard')
        #    else:
        #        messages.info(request, 'Invalid Credentials')
        #        return render(request, 'home.html')
        else:
            return render(request, 'home.html')
    return render(request, 'home.html')

def logout(request):
    logout(request)
    return redirect('/')
