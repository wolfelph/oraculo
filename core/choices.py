tipo_CHOICES = (
    ('1', 'Devol. Desligamento'),
    ('2', 'Devol. Substituição'),
    ('3', 'Novos'),
    ('4', 'DQS'),
    ('5', 'Imobilizado'),
)

modelo_CHOICES = (
    ('1', 'Lenovo Thinkpad E490'),
    ('2', 'Lenovo Thinkpad E14'),
    ('3', 'Dell 3410'),
    ('4', 'Dell 3480'),
    ('5', 'Dell 3490'),
)
processador_CHOICES = (
    ('1', 'i3'),
    ('2', 'i5'),
    ('3', 'i7'),
    ('4', 'i9'),
    ('5', 'M1'),
)
memoria_CHOICES = (
    ('1', '4GB'),
    ('2', '8GB'),
    ('3', '12GB'),
    ('4', '16GB'),
    ('5', '32GB'),
)
entrega_CHOICES = (
    ('1', 'Retirada'),
    ('2', 'Correios'),
    ('3', 'Transportadora'),
)
status_CHOICES = (
    ('1', 'Aguardando separação'),
    ('2', 'Preparando'),
    ('3', 'Falta info do user'),
    ('4', 'Aguardando retirada'),
    ('5', 'Enviado a outra filial'),
    ('6', 'Concluído'),
)

motivo_CHOICES = (
    ('1', 'Descarte'),
    ('2', 'Manutenção'),
    ('3', 'Substituição'),
    ('4', 'Onboarding'),
)