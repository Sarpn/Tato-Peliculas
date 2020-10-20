from django.shortcuts import render
from .models import Pelicula, Calificacion
from ..login.models import Usuario
from django.db.models import Avg

def index(request):

    peliculas = Pelicula.objects.all()

    return render(request, 'index.html', context={'peliculas':peliculas})


def detail(request, id):

    pelicula = Pelicula.objects.get(id=id)
    usuario = Usuario.objects.get(nombreDeUsuario = request.session['usuario'])

    if request.method == 'POST':
        valor = request.POST.get('valor', '-1')        
        Calificacion(pelicula = pelicula, usuario=usuario, valor=valor).save()
    
    calificaciones = Calificacion.objects.filter(pelicula=pelicula)
    promedio = calificaciones.aggregate(Avg('valor'))
    calificada = calificaciones.filter(usuario=usuario).exists()
    return render(request, 'detail.html', context={'pelicula':pelicula, 'calificaciones':calificaciones,'calificada':calificada, 'promedio':promedio})
