from django.db import models
from stdimage.models import StdImageField
from django.db.models import signals
from django.template.defaultfilters import slugify
from django.urls import reverse


class Base(models.Model):
    criado = models.DateField('Data de Criação', auto_now_add=True)
    modificado = models.DateField('Data de Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo', default=True)

    class Meta:
        abstract = True


class Materias(Base):
    nome = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField('Slug', max_length=250, unique=True, blank=True, editable=False)

    class Meta:
        ordering = ('nome',)
        verbose_name = 'materia'
        verbose_name_plural = 'materias'

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse(
            'Alunos:listar_alunos_por_materias',
            kwargs={
                'slug_materias': self.slug
            }
        )


class Alunos(Base):
    nome = models.CharField('Nome', max_length=200)
    idade = models.IntegerField('Idade')
    registroAcademico = models.CharField('Registro Academico', max_length=10)
    email = models.CharField('email', max_length=200)
    imagem = StdImageField('Imagem', upload_to='Aluno', variations={'thumb': (300, 300)})
    slug = models.SlugField('Slug', max_length=250, unique=True, blank=True, editable=False)
    materias = models.ForeignKey('portalAluno.Materias', verbose_name='Materias', on_delete=models.CASCADE)
    notas = models.IntegerField('Nota')


    class Meta:
        ordering = ('nome',)
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse(
            'Aluno:perfil_aluno',
            kwargs={
                'id_aluno': self.id,
                'slug_aluno': self.slug
            }
        )


def alunos_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)


def materias_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)


signals.pre_save.connect(alunos_pre_save, sender=Alunos)
signals.pre_save.connect(materias_pre_save, sender=Materias)
