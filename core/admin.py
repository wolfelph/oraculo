from django.contrib import admin

#Register your models here.

#from .models import Usuario, Equipamento, Estoque, Filial, Motivo,OutDescarte,Prestador
from .models import *


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'email')


@admin.register(Equipamento)
class EquipamentoAdmin(admin.ModelAdmin):
    list_display = (
        'eq_disponivel',
        'patrimonio',
        'modelo_equipamento',
        'processador',
        'memoria',
        'modo_entrega',
        'status',
        'avaria'
    )


@admin.register(Estoque)
class EstoqueAdmin(admin.ModelAdmin):
    list_display = ('tipo_estoque', 'filial_estoque')


@admin.register(Filial)
class FilialAdmin(admin.ModelAdmin):
    list_display = ('filial_nome',)


@admin.register(Motivo)
class MotivoAdmin(admin.ModelAdmin):
    list_display = ('motivo_saida',)


@admin.register(OutDescarte)
class OutDescarteAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'get_patrimonio', 'get_filial' )

    def get_patrimonio(self, obj):
        return obj.equipamento.patrimonio
    get_patrimonio.admin_order_field = 'patrimonio'  #Pra aparecer a foreign key do patrimonio
    get_patrimonio.short_description = 'Patrimonio'

    def get_filial(self, obj):
        return obj.equipamento.filial_nome
    get_filial.admin_order_field = 'filial_nome'
    get_filial.short_description = 'filial_nome'


@admin.register(Prestador)
class PrestadorAdmin(admin.ModelAdmin):
    list_display = ('nome_prestador',)


@admin.register(OutManutencao)
class OutManutencaoAdmin(admin.ModelAdmin):
    list_display = ('ordem_servico', 'valor', 'prestador')


@admin.register(Colaborador)
class ColaboradorAdmin(admin.ModelAdmin):
    list_display = ('cpf', 'telefone', 'endereco', 'numero_casa', 'complemento')


@admin.register(OutSubstituicao)
class OutSubstituicaoAdmin(admin.ModelAdmin):
    list_display = ('id_colab', 'ticket', 'colaborador')


@admin.register(OutOnboarding)
class OutOnboardingAdmin(admin.ModelAdmin):
    model = Equipamento
    list_display = ('id_vaga', 'dt_integracao', 'colaborador', 'get_patrimonio', 'get_filial','codigo_rastreio')

    def get_patrimonio(self, obj):
        return obj.equipamento.patrimonio
    get_patrimonio.admin_order_field = 'patrimonio'  #Pra aparecer a foreign key do patrimonio
    get_patrimonio.short_description = 'Patrimonio'

    def get_filial(self, obj):
        return obj.equipamento.filial_nome
    get_filial.admin_order_field = 'filial_nome'
    get_filial.short_description = 'filial_nome'
