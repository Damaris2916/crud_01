from django.shortcuts import render, redirect
from .models import Curso
from .forms import CursosForm

def cursos_listar(request):
    cursos = Curso.objects.all()
    contexto = {
        'lista_cursos': cursos
    }
    return render(request, 'cursos.html', contexto)

def curso_cadastro(request):
    form = CursosForm(request.POST or None)
    if form.is_valid():
            form.save()
            return redirect('cursos_listar')
    contexto = {
        'form': form
    }
    return render(request, 'curso_cadastro.html', contexto)


def curso_editar(request, id):
    curso = Curso.objects.get(pk=id)
    
    form = CursosForm(request.POST or None, instance=curso)
    if form.is_valid():
        form.save()
        return redirect('cursos_listar')
    
    contexto = {
        'form': form
    }

    return render(request, 'curso_cadastro.html', contexto)

def curso_remover(request, id):
    curso = Curso.objects.get(pk=id)
    curso.delete()
    return redirect('cursos_listar')