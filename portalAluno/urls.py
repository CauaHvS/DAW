from django.urls import path
from .views import listar_alunos, perfil_aluno

app_name = 'Alunos'

urlpatterns = [
    path('<str:id_Alunos>/<slug_Alunos>/', listar_alunos, name='detalhes_produto'),
    path('<slug_materias>/', perfil_aluno, name='listar_produtos_por_categoria'),
    path('', listar_alunos, name='listar_produtos'),
]
