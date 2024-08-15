from django.db import models

# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(max_length=40)
    email = models.EmailField()
    cpf = models.CharField(max_length=14)
    data_nascimento = models.DateField()
    imagem = models.ImageField(upload_to='capas/', null=True, blank=True)

    def __str__(self   ):
        return self.nome