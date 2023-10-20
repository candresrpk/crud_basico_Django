
from django.urls import path
from aplications.academico import views

urlpatterns = [
    path('', views.cursosHomeView, name='cursos'),
    path('crear/', views.crearCursoView, name="crear_curso"),
    path('editar/<codigo>', views.editarCursoView, name="editar_curso"),
    path('enviarEdicion/', views.enviarEdicionCurso, name="enviar_edicion"),
    path('eliminar/<codigo>', views.eliminarCursoView, name="eliminar_curso"),
]
