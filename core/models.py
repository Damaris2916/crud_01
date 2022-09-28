import email
from unittest.util import _MAX_LENGTH
from django.db import models

class Curso(models.Model):
    titulo = models.CharField('Título', max_length=100)
    vagas = models.IntegerField('Vagas')


class Emprego(models.Model):
    titulo = models.CharField('Título', max_length=100)
    vagas = models.IntegerField('Vagas')
    empresa = models.CharField('Empresa', max_length=100)
    foto = models.ImageField('Foto', upload_to='emprego', null=True)

class Cliente(models.Model):
    nome = models.CharField('Título', max_length=100)
    telefone = models.CharField('Telefone', max_length=12)
    email = models.CharField('Email', max_length=100)
    endereco = models.CharField('Endereco', max_length=250)
    foto = models.ImageField('Foto', upload_to='cliente', null=True) 