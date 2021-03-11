from django.core.exceptions import ValidationError

def validar_cpf(valor):
    if valor < 10000000 or valor > 99999999999 :
        raise ValidationError(('O valor digitado não é um número de CPF válido'))