from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from  django.contrib.auth.models import User
from django.contrib.auth import login , logout,authenticate
from django.db import IntegrityError


def menu(request):
    return render(request, 'menu.html')

def sobreMi(request):
    return render(request, 'sobreMi.html')

def blog(request):
    return render(request, 'blog.html')

def contacto(request):
    return render(request, 'contacto.html')

def signup(request):

    if request.method == 'GET':
        return render(request , 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(usernama=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect ('login')
            except IntegrityError:
                return render(request , 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'Usuario ya existente'
                })
        return render(request , 'signup.html', {
            'form': UserCreationForm,
            'error': 'Contraseña no coinciden'
        })
    
def signout(request):
    logout(request)
    return redirect('login')

def sigin(request):
    if request.method == 'GET':
        return render (request, 'login.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'],password=request.POST['password'])
        if user is None: 
            return render (request, 'login.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o contraseña incorrecta',
            })
        else:
            login(request,user)
            return redirect('menu')

        