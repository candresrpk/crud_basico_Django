from django.shortcuts import render, redirect
from aplications.academico.models import Curso
from django.contrib import messages
# Create your views here.


def cursosHomeView(request):
    cursos = Curso.objects.all()

    context = {
        "cursos":cursos
    }

    return render(request, './cursos/cursos.html', context)


def crearCursoView( request):
    codigo = request.POST["txtCodigo"]
    nombre = request.POST["txtNombre"]
    creditos = request.POST["txtCreditos"]

    try:
        curso = Curso.objects.create(
            codigo=codigo,
            nombre=nombre,
            creditos=creditos
        )
        curso.save()
        messages.success(request, "Se ha creado el curso satisfactoriamente!")
        return redirect('cursos')
    except Exception as e:
        messages.success(request, "No se ha podido creado el curso :(")
        return redirect('cursos')



def editarCursoView(request, codigo):
    curso = Curso.objects.get(codigo=codigo)

    context = {
        'curso':curso
    }

    return render(request, "./cursos/editarCurso.html", context)


def enviarEdicionCurso(request):
    codigo = request.POST["txtCodigo"]
    nombre = request.POST["txtNombre"]
    creditos = request.POST["txtCreditos"]
    try:
        curso = Curso.objects.get(codigo=codigo)
        curso.nombre=nombre
        curso.creditos=creditos
        curso.save()

        messages.success(request, "Se ha actualizado el curso satisfactoriamente!")
        return redirect('cursos')
    except Exception as e:
        return {'message': f'something whent wrong {e}',}



def eliminarCursoView(request, codigo):

    try:
        curso = Curso.objects.get(codigo=codigo)
        curso.delete()
        messages.success(request, "Se ha eliminado el curso satisfactoriamente!")
        return redirect('cursos')
    except Exception as e:
        messages.error(request, "No se ha podido eliminar")
        return redirect('cursos')

