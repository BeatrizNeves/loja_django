from django.urls import path
from catalogo import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.ProdutosView.as_view(), name='produto'),
    path('<int:pk>', views.ProdutoDetalhadoView.as_view(), name='produto-detalhado'),
    path('categoria/<int:id_categoria>', views.ProdutoPorCategoriaView.as_view(), name='produto-categoria'),
    path('<int:id_produto>/compra/', views.realiza_compra, name='realiza-compra'),
    path('compra_realizada/<int:id_compra>', views.compra_realizada, name='compra-realizada'),
    path('cadastro_produtos_menu/', views.cadastro_produtos_menu, name='cadastro-produtos-menu'),
    path('editar_produto/<int:id_produto>', views.editar_produto, name='editar-produto'),
    path('cadastro_produto', views.cadastro_produto, name='cadastro-produto'),
    path('estatisticas', views.estatisticas, name='estatisticas'),
]