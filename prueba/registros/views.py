
from urllib import request
from django.shortcuts import render
from .models import Alumnos
from .forms import ComentarioContactoForm, Usuario
from .models import ComentarioContacto
from django.shortcuts import get_object_or_404

# Create your views here.
def registros(request):
    alumnos= Alumnos.objects.all()
#all recupera todos los objetos del modelo  (registros de la tabla alumnos)
    return render(request, "registros/principal.html" ,{'alumnos':alumnos})
#Indicamos el lugar donde se renderizará el resultado de esta vista
# y enviamos la lista de alumnos recuparados

def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid(): #Si los datos recibidos son correctos
            form.save() #Inserta
            comentarios = ComentarioContacto.objects.all()
            return render(request, "registros/comentariosRegistrados.html",{'comentarios': comentarios})
    form = ComentarioContactoForm()
    #Si salgo sale mal se reenvian al formulario los datos ingresados
    return render(request, 'registros/contacto.html', {'form':form})

def contacto(request):
    return render(request, "registros/contacto.html")
    #Indicamos el lugar donde se renderizará el resultado de esta vista
    #Enviamos la lista de alumnos recuperados.

def comentariosRegistrados(request):
    comentarios = ComentarioContacto.objects.all()
    return render(request, "registros/comentariosRegistrados.html",{'comentarios': comentarios})

def eliminarComentarioContacto(request, id,
    confirmacion='registros/confirmarEliminacion.html'):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    if request.method=='POST':
        comentario.delete()
        comentarios=ComentarioContacto.objects.all()
        return render(request, "registros/comentariosRegistrados.html",
            {'comentarios': comentarios})
    return render(request, confirmacion, {'object':comentario})

def consultarComentario(request, id):
    comentario = ComentarioContacto.objects.get(id=id)
    return render(request, 'registros/formEditarComentario.html', {'comentario': comentario})

def editarComentario(request, id):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    form = ComentarioContactoForm(request.POST, instance=comentario)
    
    if form.is_valid():
        form.save()
        comentarios = ComentarioContacto.objects.all()
        return render(request, 'registros/comentariosRegistrados.html', {'comentarios': comentarios})
    return render(request, 'registros/formEditarComentario.html', {'comentario':comentario })

def eliminarUsuario(request, id, confirmacion= 'registros/eliminarUsuario.html'):
    alumno= Alumnos.objects.get(id=id)
    if request.method=='POST':
        alumno.delete()
        alumnos = Alumnos.objects.all()
        return render(request,"registros/principal.html" ,{'alumnos':alumnos},)
    return render(request, confirmacion, {'object':alumno})

def editarUsuario(request, id):
    alumno = get_object_or_404(Alumnos, id=id)
    form = Usuario(request.POST, instance=alumno)
    
    if form.is_valid():
        form.save()
        alumnos = Alumnos.objects.all()
        return render(request, 'registros/principal.html', {'alumnos': alumnos})
    return render(request, 'registros/editarUsuario.html', {'alumno':alumno })

def actualizarUsuario(request,id):
    alumno = Alumnos.objects.get(id=id)
    return render(request, 'registros/editarUsuario.html', {'alumno': alumno})

# def actualizarUsuario(request, id):
#     alumno = Alumnos.objects.get(id=id)
#     return render(request, 'registros/editarUsuario.html', {'alumno': alumno})

# def editarUsuario(request, id):
#     alumno = get_object_or_404(Alumnos, id=id)
#     form = Usuario(request.POST, instance=alumno)
    
#     if form.is_valid():
#         form.save()
#         alumnos = Alumnos.objects.all()
#         return render(request, 'registros/principal.html', {'alumnos': alumnos})
#     return render(request, 'registros/editarUsuario.html', {'alumno':alumno })

