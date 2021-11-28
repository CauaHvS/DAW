from django.shortcuts import render, get_object_or_404
from .models import Alunos, Materias


def listar_alunos(request, slug_materias=None):
    materias = None
    lista_materias = Materias.objects.all()
    lista_alunos = Alunos.objects.filter(ativo=True)
    if slug_materias:
        materias = get_object_or_404(materias, slug=slug_materias)
        lista_alunos = Alunos.objects.filter(categoria=Materias)
    contexto = {
        'Marerias': materias,
        'lista_materias': lista_materias,
        'lista_alunos': lista_alunos,
    }
    return render(request, 'aluno/portalAluno.html', contexto)


def perfil_aluno(request, id_aluno, slug_aluno):

    alunos = get_object_or_404(Alunos,
                                id=id_aluno,
                                slug=slug_aluno,
                                ativo=True)
    contexto = {
        'Aluno': alunos,
    }
    return render(request, 'produtos/detalhes.html', contexto)


