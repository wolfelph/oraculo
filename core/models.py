from django.db import models

from core.choices import *

class Filial(models.Model):
    filial_nome = models.CharField(max_length=50, default="7004-Franca")
    filial_estoque = models.CharField('Filial', max_length=50, default=1)

    class Meta:
        verbose_name = 'Filial'
        verbose_name_plural = 'Filiais'


class Estoque(models.Model):

    tipo_estoque = models.CharField('Tipo de Estoque', max_length=50, choices=tipo_CHOICES)
    filial_estoque = models.ForeignKey('Filial', on_delete=models.CASCADE)

    def __str__(self):
        return self.filial_estoque.filial_nome # Retornando FK

    class Meta:
        verbose_name = 'Estoque'
        verbose_name_plural = 'Estoque'


class Usuario(models.Model):
    # Ver opções de id, autofield, integerfield
    usuario = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    filial_nome = models.CharField(max_length=50, default="7004-Franca")
    last_login = models.DateTimeField(auto_now=False, auto_now_add=False)
    date_joined = models.DateTimeField(auto_created=False, auto_now_add=False)
    dtchange_password = models.DateTimeField()
    # imagem = models.ImageField('Imagem', upload_to=get_file_path, variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})

    def __str__(self):
        return self.usuario, self.first_name, self.last_name, self.email



"""
class Avaria(models.Model):
  descricao_avaria: models.CharField(max_length=500)
     def __str__(self):
          return self.descricao_avaria  # Retorna a classe toda
    
     class Meta:
        verbose_name = 'Avaria'
        verbose_name_plural = 'Avarias'
"""


class Equipamento(models.Model):

    eq_disponivel = models.BooleanField()
    filial_nome = models.CharField(max_length=50, default="7004-Franca")
    patrimonio = models.PositiveIntegerField()
    modelo_equipamento = models.CharField('Modelo', max_length=50, choices=modelo_CHOICES)
    processador = models.CharField('Processador', max_length=50, choices=processador_CHOICES)
    memoria = models.CharField('Memória', max_length=50, choices=memoria_CHOICES)
    modo_entrega = models.CharField('Modo de Envio', max_length=50, choices=entrega_CHOICES)
    status = models.CharField('Status', max_length=50, choices=status_CHOICES)
    avaria = models.CharField('Avaria', max_length=150)
    tipo_estoque = models.ForeignKey(Estoque, on_delete=models.CASCADE, default=1)
    data_entrada = models.DateField('Data da entrada', max_length=50)

    def __str__(self):
        return str(self.patrimonio)  # Permite aparecer o nome ao inves do object1 pra int

    class Meta:
        verbose_name = 'Equipamento'
        verbose_name_plural = 'Equipamentos'


class EntradaSubstituicao(Equipamento):
    nome_colaborador = models.CharField('Nome do colaborador', max_length=50)
    id_colaborador = models.IntegerField()
    ticket = models.IntegerField()

    class Meta:
        verbose_name = 'Entrada Substituição'
        verbose_name_plural = 'Entradas de Substituições'


class EntradaOnboarding(Equipamento):
    nome_colaborador = models.CharField('Nome do colaborador', max_length=50)
    id_colaborador = models.IntegerField()


    class Meta:
        verbose_name = 'Entrada Onboarding'
        verbose_name_plural = 'Entradas de Onboarding'


class EntradaNovos(Equipamento):
    nota_fiscal = models.CharField('Nota Fiscal', max_length=30)

    class Meta:
        verbose_name = 'Entrada Novo'
        verbose_name_plural = 'Entradas de Novos Equipamentos'


class Motivo(models.Model):

    motivo_saida = models.CharField('Motivo Saída', max_length=50, choices=motivo_CHOICES)
    filial_nome = models.CharField(max_length=50, default="7004-Franca")



    class Meta:
        verbose_name = 'Motivo'
        verbose_name_plural = 'Motivo'


class OutDescarte(models.Model):
    descricao = models.CharField('Descreva brevemente', max_length=100)
    equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE)  # Chave estrangeira
    filial_nome = models.CharField(max_length=50, default="7004-Franca")

    class Meta:
        verbose_name = 'Descarte'
        verbose_name_plural = 'Descartes'


class Prestador(models.Model):
    nome_prestador = models.CharField(max_length=100)
    filial_nome = models.CharField(max_length=50, default="7004-Franca")

    def __str__(self):
        return self.nome_prestador  # Retornando FK

    class Meta:
        verbose_name = 'Prestador'
        verbose_name_plural = 'Prestadores'


class OutManutencao(Motivo):
    ordem_servico = models.PositiveIntegerField()
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    prestador = models.ForeignKey(Prestador, on_delete=models.CASCADE)  # Chave estrangeira

    def __str__(self):
        return self.prestador  # Permite aparecer o nome ao inves do object1

    class Meta:
        verbose_name = 'Manutenção'
        verbose_name_plural = 'Manutenções'


class Colaborador(models.Model):
    nome_colab = models.CharField(max_length=100)
    cpf = models.IntegerField(unique=True)  # Fazer normalização
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=100)
    numero_casa = models.IntegerField()
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    cep = models.IntegerField()
    complemento = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    filial_nome = models.CharField(max_length=50, default="7004-Franca")# FK

    def __str__(self):
        return self.nome_colab # Permite aparecer o nome ao inves do object1

    class Meta:
        verbose_name = 'Colaborador'
        verbose_name_plural = 'Colaboradores'


class OutSubstituicao(Motivo):
    id_colab = models.IntegerField()
    ticket = models.CharField(max_length=15)
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE)
    patrimonio_devolvido = models.CharField('Patrimônio devolvido', max_length=10)
    equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE)
    codigo_rastreio = models.CharField(max_length=13, blank=True)# Permite o campo ficar vazio

    def __str__(self):
        return self.colaborador  # Permite aparecer o nome ao inves do object1

    class Meta:
        verbose_name = 'Substituição'
        verbose_name_plural = 'Substituições'


class OutOnboarding(Motivo):
    id_vaga = models.IntegerField()
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE)
    dt_integracao = models.DateField()
    equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE)
    codigo_rastreio = models.CharField(max_length=13, blank=True)

    def __str__(self):
        return self.colaborador # Permite aparecer o nome ao inves do object1

    class Meta:
        verbose_name = 'Onboarding'
        verbose_name_plural = 'Onboarding'
