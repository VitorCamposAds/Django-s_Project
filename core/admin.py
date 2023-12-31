from django.contrib import admin
from .models import Cargo, Servico, Funcionario

from .models import Features

'''
class AdminArea(admin.AdminSite):
    site_header = 'Projeto Vitor'

projeto_vitor = AdminArea(name='Administração Projeto Vitor')
'''

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'ativo', 'modificado')

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('servico', 'icone', 'ativo', 'modificado')

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'modificado')

@admin.register(Features)
class FeaturesAdmin(admin.ModelAdmin):
    list_display = ('feature', 'descricao', 'icone')