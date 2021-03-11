from django.shortcuts import render
from catalogo.models import Categoria, Produto, Usuario, Compra
from django.views import generic
from catalogo.forms import RealizarCompraForm
from catalogo.forms import CadastroProdutoForm
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime


class ProdutosView(generic.ListView):
    model = Produto
    
    def get_context_data(self, **kwargs):
        context = super(ProdutosView, self).get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        return context
        
    
    """num_produtos = Produto.objects.count()
    num_categorias = Categoria.objects.count()
    
    context = {
        'num_produtos': num_produtos,
        'num_categorias': num_categorias,
    }
    
    return render(request, 'index.html', context=context)"""
    
    
class ProdutoDetalhadoView(generic.DetailView):
    model = Produto
    
    def get_context_data(self, **kwargs):
        context = super(ProdutoDetalhadoView, self).get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        return context
        
        
class ProdutoPorCategoriaView(generic.ListView):
    model = Produto
    
    def get_queryset(self):
        return Produto.objects.filter(categoria__exact=self.kwargs['id_categoria'])
        
    def get_context_data(self, **kwargs):
        context = super(ProdutoPorCategoriaView, self).get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        return context
        
        
def realiza_compra(request, id_produto):
    produto = get_object_or_404(Produto, pk=id_produto)

    if request.method == 'POST':
        form = RealizarCompraForm(request.POST)

        if form.is_valid():
            produto.estoque = produto.estoque - form.cleaned_data['quantidade']
            produto.save()
            
            usuario = Usuario.objects.create(nome=form.cleaned_data['nome'], endereco=form.cleaned_data['endereco'], email=form.cleaned_data['email'], cpf=form.cleaned_data['cpf'])
            
            compra = Compra.objects.create(data=datetime.date.today(), usuario=usuario, produto=produto, quantidade=form.cleaned_data['quantidade'])

            return HttpResponseRedirect(reverse('compra-realizada', kwargs={'id_compra':compra.pk}))

    else:
        form = RealizarCompraForm()

    context = {
        'form': form,
        'categorias': Categoria.objects.all(),
        'produto': produto,
    }
    
    return render(request, 'catalogo/realiza_compra.html', context)
    
    
def compra_realizada(request, id_compra):
    compra = get_object_or_404(Compra, pk=id_compra)
    produto = get_object_or_404(Produto, pk=compra.produto.pk)
    usuario = get_object_or_404(Usuario, pk=compra.usuario.pk)
    
    preco_total = compra.quantidade * produto.preco

    context = {
        'categorias': Categoria.objects.all(),
        'compra': compra,
        'usuario': usuario,
        'preco_total': preco_total,
    }
    return render(request, 'catalogo/compra_realizada.html', context)
    
    
def cadastro_produtos_menu(request):
    context = {
        'produto_list': Produto.objects.all(),
    }
    return render(request, 'catalogo/cadastro_produtos_list.html', context)
    
    
def editar_produto(request, id_produto):
    produto = get_object_or_404(Produto, pk=id_produto)

    if request.method == 'POST':
        form = CadastroProdutoForm(request.POST)

        if form.is_valid():
            produto.nome = form.cleaned_data['nome']
            produto.foto = form.cleaned_data['foto']
            produto.categoria = form.cleaned_data['categoria']
            produto.descricao = form.cleaned_data['descricao']
            produto.preco = form.cleaned_data['preco']
            produto.estoque = form.cleaned_data['estoque']
            produto.save()
            
            return HttpResponseRedirect(reverse('cadastro-produtos-menu'))

    else:
        
        form = CadastroProdutoForm(initial={'nome': produto.nome, 'foto': produto.foto, 'categoria': produto.categoria.pk, 'descricao': produto.descricao,'preco': produto.preco,'estoque': produto.estoque})

    context = {
        'form': form,
        'produto': produto,
    }
    
    return render(request, 'catalogo/edita_produto.html', context)
    
    
    
def cadastro_produto(request):

    if request.method == 'POST':
        form = CadastroProdutoForm(request.POST)

        if form.is_valid():
            produto = Produto.objects.create(nome=form.cleaned_data['nome'],foto=form.cleaned_data['foto'],categoria=form.cleaned_data['categoria'],descricao=form.cleaned_data['descricao'],preco=form.cleaned_data['preco'],estoque=form.cleaned_data['estoque'])
            
            return HttpResponseRedirect(reverse('cadastro-produtos-menu'))

    else:
        form = CadastroProdutoForm()

    context = {
        'form': form
    }
    
    return render(request, 'catalogo/cadastro_produto.html', context)
    
    
def estatisticas(request):
    categorias = Categoria.objects.all()

    for categoria in categorias:
        categoria.quantidade = 0
        categoria.valor_total = 0
        categoria.quantidade_vendas = 0
        produtos = Produto.objects.filter(categoria=categoria)
        for produto in produtos:
            compras = Compra.objects.filter(produto=produto)
            for compra in compras:
                categoria.quantidade_vendas = categoria.quantidade_vendas + 1
                categoria.quantidade = categoria.quantidade + compra.quantidade
                categoria.valor_total = categoria.valor_total + (compra.quantidade * produto.preco)
                
    context = {
        'categorias': categorias,
    }
    
    return render(request, 'catalogo/estatisticas.html', context)