from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm #UserCreationForm,
from  django.contrib.auth.models import User
from django.contrib.auth import login , logout,authenticate, update_session_auth_hash
from django.db import IntegrityError
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm,UserEditForm, ChangePasswordForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from FutbolMundial.forms import UserEditForm, ChangePasswordForm , AvatarForm



@login_required
def menu(request):
    avatar = getavatar(request)
    return render(request, "menu.html", {"avatar": avatar})



@login_required
def sobreMi(request):
    avatar = getavatar(request)
    return render(request, 'sobreMi.html', {"avatar": avatar})




@login_required
def blog(request):
        
        futbol = Autores.objects.all()
        pages = Page.objects.all()

        if request.method == "POST":
            nombre = request.POST["nombre"]
            mensaje = request.POST["mensaje"]
            obj = Comentario(nombre=nombre, comentario=mensaje)
            obj.save()
            mensaje = "Gracias por tu comentario!"
            return render (request,"blog.html" , {"futbol": futbol, "pages": pages,"mensaje":mensaje} )
        return render(request, "blog.html",  {"futbol" : futbol ,"pages": pages,} )

    #return render(request, 'blog.html')




@login_required
def contacto(request):
    
    futbol = Autores.objects.all()
    pages = Page.objects.all()

    if request.method == "POST":
        nombre = request.POST["nombre"]
        mensaje = request.POST["mensaje"]
        obj = Comentario(nombre=nombre, comentario=mensaje)
        obj.save()
        mensaje = "Gracias por tu comentario!"
        return render (request,"contacto.html" , {"futbol": futbol, "pages": pages,"mensaje":mensaje})
    return render(request, "contacto.html", {"futbol" : futbol ,"pages": pages,} )



def signup(request):

    if request.method == 'GET':
        return render(request , 'signup.html', {
            'form': CustomUserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],  email=request.POST['email'], password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect ('login')
            except IntegrityError:
                return render(request , 'signup.html', {
                    'form': CustomUserCreationForm,
                    'error': 'Usuario ya existente'
                })
        return render(request , 'signup.html', {
            'form': CustomUserCreationForm,
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



@login_required    
def perfil(request):
    avatar = getavatar(request)
    return render (request,"perfil.html", {"avatar": avatar})



def page_detail(request, pageId):
    page = Page.objects.get(id=pageId)
    return render(request, 'page_detail.html', {'page': page})



class AutorList(ListView):

    model = Autores
    template_name = "autor_list.html"
    

class AutorDetalle(DetailView):
    model = Autores
    template_name = "autor_detalle.html"

class AutorCreacion(CreateView):
    model = Autores
    template_name = "autor_form.html"
    success_url = "/FutbolMundial/autor/list"
    fields = ["nombre"]

class AutorUpdate(UpdateView):
    model = Autores
    template_name = "autor_form.html"
    success_url = "/FutbolMundial/autor/list"
    fields = ["nombre"]

class AutorDelete(DeleteView):
    model = Autores
    template_name = "autor_confirm_delete.html"
    success_url = "/FutbolMundial/autor/list"

@login_required
def perfilview(request):
    
    user = request.user
    return render(request, 'perfil.html', {'user': user} )
   
@login_required  
def editarPerfil(request):
    
    usuario = request.user
    user_basic_info = User.objects.get(id = usuario.id)
    if request.method == "POST":
        form = UserEditForm(request.POST, instance = usuario)
        if form.is_valid():
            user_basic_info.username = form.cleaned_data.get('username')
            user_basic_info.email = form.cleaned_data.get('email')
            user_basic_info.first_name = form.cleaned_data.get('first_name')
            user_basic_info.last_name = form.cleaned_data.get('last_name')
            user_basic_info.save()
            return render(request, 'Perfil.html', )
    else:
        form = UserEditForm(initial= {'username': usuario.username, 'email': usuario.email, 'first_name': usuario.first_name, 'last_name': usuario.last_name })
        return render(request, 'editarPerfil.html', {"form": form})

@login_required
def changePassword(request):
    usuario = request.user    
    if request.method == "POST":
        form = ChangePasswordForm(data = request.POST, user = usuario)
        if form.is_valid():
            if request.POST['new_password1'] == request.POST['new_password2']:
                user = form.save()
                update_session_auth_hash(request, user)
            return HttpResponse("Las constraseñas no coinciden")
        return render(request, "menu.html")
    else:
        form = ChangePasswordForm(user = usuario)
        return render(request, 'changePassword.html', {"form": form})
    
def getavatar(request):
    avatar = Avatar.objects.filter(user = request.user.id)
    try:
        avatar = avatar[0].image.url
    except:
        avatar = None
    return avatar

def editAvatar(request):
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES)
        print(form)
        print(form.is_valid())
        if form.is_valid():
            user = User.objects.get(username = request.user)
            avatar = Avatar(user = user, image = form.cleaned_data['avatar'], id = request.user.id)
            avatar.save()
            avatar = Avatar.objects.filter(user = request.user.id)
            try:
                avatar = avatar[0].image.url
            except:
                avatar = None           
            return render(request, "menu.html", {'avatar': avatar})
    else:
        try:
            avatar = Avatar.objects.filter(user = request.user.id)
            form = AvatarForm()
        except:
            form = AvatarForm()
    return render(request, "avatar.html", {'form': form})
