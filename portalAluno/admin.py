from django.contrib import admin
from .models import Alunos, Materias


@admin.register(Alunos)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'materias', 'idade', 'registroAcademico', 'notas', 'email', 'slug', 'criado', 'modificado', 'ativo']


@admin.register(Materias)
class MateriasAdmin(admin.ModelAdmin):
    list_display = ['nome', 'slug']