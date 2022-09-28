"""crud_01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from core.views import cursos_listar, curso_cadastro, curso_editar, curso_remover, emprego_cadastro, emprego_editar,emprego_listar,emprego_remover, cliente_listar,cliente_cadastro,cliente_editar,cliente_remover,home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),


    path('cursos/', cursos_listar, name='cursos_listar'),
    path('cliente/', cliente_listar, name= 'clientes_listar'),
    path('emprego/', emprego_listar,name= 'empregos_listar'),

    path('emprego_cadastro/', emprego_cadastro, name='empregos_cadastro'),
    path('cliente_cadastro/', cliente_cadastro, name='clientes_cadastro'),
    path('curso_cadastro/', curso_cadastro, name='cursos_cadastro'),
    
    path('curso_editar/<int:id>/', curso_editar, name='curso_editar'),
    path('cliente_editar/<int:id>/', cliente_editar, name='cliente_editar'),
    path('emprego_editar/<int:id>/', emprego_editar, name='emprego_editar'),

    path('curso_remover/<int:id>/', curso_remover, name='curso_remover'),
    path('cliente_remover/<int:id>/', cliente_remover, name='cliente_remover'),
    path('emprego_remover/<int:id>/', emprego_remover, name='emprego_remover'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
