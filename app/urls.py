
from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),

    path('produtos/', ProdutoView.as_view(), name='produtos'),
    path('tipos-produtos/', TipoProdutoView.as_view(), name='tipos_produtos'),
    path('materiais/', MaterialView.as_view(), name='materiais'),
    path('fornecedores/', FornecedorView.as_view(), name='fornecedores'),
    path('clientes/', ClienteView.as_view(), name='clientes'),

    path('vendas/', VendaView.as_view(), name='vendas'),
    path('itens-vendas/', ItemVendaView.as_view(), name='itens_vendas'),

    path('estoques/', EstoqueView.as_view(), name='estoques'),
    path('entradas-produtos/', EntradaProdutoView.as_view(), name='entradas_produtos'),

    path('pedras/', PedraView.as_view(), name='pedras'),

    path('cidades/', CidadeView.as_view(), name='cidades'),
    path('ufs/', UFView.as_view(), name='ufs'),
]
