from django.db import models
from django.urls import reverse
from catalogo.validators import validar_cpf
import uuid 

# Create your models here.


class Categoria(models.Model):
    nome = models.CharField(max_length=200, help_text='Categoria de produto')

    def __str__(self):
        return self.nome
        
    class Meta:
        ordering = ['nome']
        
class Produto(models.Model):
    nome = models.CharField(max_length=200, help_text='Nome do produto')
    foto = models.CharField(max_length=400, help_text='Link para foto do produto', null=True)
    categoria = models.ForeignKey('Categoria', on_delete=models.SET_NULL, null=True, help_text='Categoria ao qual pertence o produto')
    descricao = models.TextField(max_length=1000, help_text='Descrição do produto')
    preco = models.DecimalField(max_digits=9, decimal_places=2, help_text='Preço do produto')
    estoque = models.IntegerField(help_text='Quantidade em estoque do produto')

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('produto-detalhado', args=[str(self.id)])
        
    class Meta:
        ordering = ['nome']
        
class Usuario(models.Model):
    nome = models.CharField(max_length=200, help_text='Nome do comprador')
    endereco = models.CharField(max_length=200, help_text='Endereço para entrega da compra')
    email = models.EmailField(max_length=200, help_text='E-mail de contato do comprador')
    cpf = models.PositiveIntegerField(help_text='CPF do comprador', validators=[validar_cpf])

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('usuario-detalhado', args=[str(self.id)])
        
    class Meta:
        ordering = ['nome']
        
class Compra(models.Model):
    data = models.DateField(help_text='Data em que a compra foi realizada')    
    usuario = models.ForeignKey('Usuario', on_delete=models.SET_NULL, null=True, help_text='Usuário responsável pela compra')
    produto = models.ForeignKey('Produto', on_delete=models.SET_NULL, null=True, help_text='Produto comprado')
    quantidade = models.IntegerField(help_text='Quantidade comprada do produto')

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('compra-detalhado', args=[str(self.id)])

    class Meta:
        ordering = ['data'] 