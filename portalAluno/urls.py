from django.urls import path
from .views import listar_alunos, perfil_aluno

app_name = 'Alunos'

urlpatterns = [
    path('<str:id_aluno>/<slug_aluno>/', perfil_aluno, name='perfil_aluno'),
    path('<slug_materias>/', listar_alunos, name='listar_alunos_por_materia'),
    path('', listar_alunos, name='listar_alunos'),
]
