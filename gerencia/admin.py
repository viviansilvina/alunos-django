from django.contrib import admin
from .models import Aluno
from django.utils.html import format_html

# Register your models here.
@admin.register(Aluno)
class AlunoAdmmin(admin.ModelAdmin):
    def image_tag(self,obj):
        return format_html('<img src= "{}" style="max-width:200px;max-height:200px"/>'.format(obj.imagem.url))
    
    image_tag.short_description = 'Imagem'
    list_display = ['nome', 'email', 'cpf', 'data_nascimento', 'image_tag']
    list_filter = ['nome', 'email', 'cpf', 'data_nascimento',]