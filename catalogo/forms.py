from django import forms
from catalogo.models import Categoria
from catalogo.validators import validar_cpf

class RealizarCompraForm(forms.Form):
    nome = forms.CharField(max_length=200, help_text='Nome do comprador')
    endereco = forms.CharField(max_length=200, help_text='Endereço para entrega da compra', label='Endereço')
    email = forms.EmailField(max_length=200, help_text='E-mail de contato do comprador', label='E-mail')
    cpf = forms.IntegerField(help_text='CPF do comprador (apenas os números)', label='CPF', validators=[validar_cpf])
    quantidade = forms.IntegerField(help_text='Quantidade que deseja comprar do produto')
    
    
    
class CadastroProdutoForm(forms.Form):
    nome = forms.CharField(max_length=200, help_text='Nome do produto')
    foto = forms.CharField(max_length=400, help_text='Link para foto do produto')
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), help_text='ID da categoria ao qual pertence o produto')
    descricao = forms.CharField(max_length=1000, help_text='Descrição do produto')
    preco = forms.DecimalField(max_digits=9, decimal_places=2, help_text='Preço do produto')
    estoque = forms.IntegerField(help_text='Quantidade em estoque do produto')