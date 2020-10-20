from django.shortcuts import render, redirect
from .models import Usuario

# Create your views here.

def login(request):

    if request.method == 'POST':   
        user = request.POST.get('user')
        password = request.POST.get('password')

        if Usuario.objects.filter(nombreDeUsuario=user, password=password).exists():
           usuario = Usuario.objects.get(nombreDeUsuario=user, password=password)
           
           request.session['nombre'] = usuario.nombre
           request.session['usuario'] = usuario.nombreDeUsuario

           return redirect('index')
        else:
            return render(request,'login.html',context={'mensaje':'Los sentimos, sus credenciales no son válidas'})
    else:
        return render(request,'login.html')
