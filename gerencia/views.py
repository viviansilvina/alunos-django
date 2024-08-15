from django.shortcuts import render
from .models import Aluno
# Create your views here.
def index(request):
    alunos = Aluno.objects.all()
    contexto = {
        'lista': alunos
    }
    return render(request, 'alunos/index.html', contexto)

def detalhe_aluno(request, aluno_id):
    alunos = Aluno.objects.get(id=aluno_id)
    contexto ={
        'aluno': alunos
    }
    return render(request, 'alunos/detalhe_aluno.html', contexto)