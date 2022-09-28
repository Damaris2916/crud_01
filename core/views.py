from django.shortcuts import render, redirect
from .models import Curso, Emprego, Cliente
from .forms import CursosForm, ClienteForm, EmpregoForm

def home(request):
    return render(request, 'index.html')

    
def cursos_listar(request):
    cursos = Curso.objects.all()
    contexto = {
        'lista_cursos': cursos
    }
    return render(request, 'cursos.html', contexto)

def emprego_listar(request):
    empregos = Emprego.objects.all()
    contexto = {
        'lista_empregos': empregos
    }
    return render(request, 'Emprego.html', contexto)

def cliente_listar(request):
    clientes = Cliente.objects.all()
    contexto = {
        'lista_clientes': clientes
    }
    return render(request, 'cliente.html', contexto)


def emprego_cadastro(request):
    form = EmpregoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
            form.save()
            return redirect('empregos_listar')
    contexto = {
        'form': form
    }
    return render(request, 'emprego_cadastro.html', contexto)

def curso_cadastro(request):
    form = CursosForm(request.POST or None, request.FILES or None)
    if form.is_valid():
            form.save()
            return redirect('cursos_listar')
    contexto = {
        'form': form
    }
    return render(request, 'curso_cadastro.html', contexto)

def cliente_cadastro(request):
    form = ClienteForm(request.POST or None, request.FILES or None)
    if form.is_valid():
            form.save()
            return redirect('clientes_listar')
    contexto = {
        'form': form
    }
    return render(request, 'cliente_cadastro.html', contexto)



def curso_editar(request, id):
    curso = Curso.objects.get(pk=id)
    
    form = CursosForm(request.POST or None, request.FILES or None,instance=curso)
    if form.is_valid():
        form.save()
        return redirect('cursos_listar')
    
    contexto = {
        'form': form
    }

    return render(request, 'curso_cadastro.html', contexto)

def emprego_editar(request, id):
    emprego = Emprego.objects.get(pk=id)
    
    form = EmpregoForm(request.POST or None,request.FILES or None, instance=emprego)
    if form.is_valid():
        form.save()
        return redirect('empregos_listar')
    
    contexto = {
        'form': form
    }

    return render(request, 'emprego_cadastro.html', contexto)

def cliente_editar(request, id):
    clientes = Cliente.objects.get(pk=id)
    
    form = ClienteForm(request.POST or None, request.FILES or None, instance=clientes)
    if form.is_valid():
        form.save()
        return redirect('clientes_listar')
    
    contexto = {
        'form': form
    }

    return render(request, 'cliente_cadastro.html', contexto)


def curso_remover(request, id):
    curso = Curso.objects.get(pk=id)
    curso.delete()
    return redirect('cursos_listar')

def emprego_remover(request, id):
    empregos = Emprego.objects.get(pk=id)
    empregos.delete()
    return redirect('empregos_listar')

def cliente_remover(request, id):
    clientes = Cliente.objects.get(pk=id)
    clientes.delete()
    return redirect('clientes_listar')