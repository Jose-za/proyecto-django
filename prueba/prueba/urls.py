"""prueba URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inicio import views
from django.conf import settings
#permite acceder a las variables MEDIA_URL Y MEDIA_ROOT que almacenan la
#ubicacion de nuestras imagenes
from registros import views as views_registros
#Importamos la nueva vista de app registros para poder asignar las rutas de acceso a sus vistas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views_registros.registros, name = "Principal"),
    path('contacto/', views_registros.contacto, name="Contacto"),
    path('formulario/', views.formulario, name="Formulario"),
    path('ejemplo/', views.ejemplo, name="Ejemplo"),
    path('registrar/', views_registros.registrar, name="Registrar"),
    path('consultarComentario/', views_registros.comentariosRegistrados, name="Comentario"),
    path('eliminarComentario/<int:id>/',views_registros.eliminarComentarioContacto,name='Eliminar'),
    path('editarComentario/<int:id>/',views_registros.editarComentario,name='Editar'),
    path('formEditarComentario/<int:id>/',views_registros.consultarComentario,name='ConsultaIndividual'),

    path('eliminarUsuario/<int:id>/',views_registros.eliminarUsuario,name='EliminarUsuario'),
    path('ActualizarUsuario/<int:id>/',views_registros.editarUsuario,name='ActualizarAlumnos'),
    path('editarUsuario/<int:id>/',views_registros.actualizarUsuario,name='EditarUsuario'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)