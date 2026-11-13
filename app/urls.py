
from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),

    # Produtos
    path('produtos/', ProdutoView.as_view(), name='produtos'),
    path('produtos/adicionar/', ProdutoAdicionarView.as_view(), name='adicionar_produto'),

    # Tipos de produtos
    path('tipos-produtos/', TipoProdutoView.as_view(), name='tipos_produtos'),
    path('tipos-produtos/adicionar/', TipoProdutoAdicionarView.as_view(), name='adicionar_tipo_produto'),

    # Materiais
    path('materiais/', MaterialView.as_view(), name='materiais'),
    path('materiais/adicionar/', MaterialAdicionarView.as_view(), name='adicionar_material'),

    # Fornecedores
    path('fornecedores/', FornecedorView.as_view(), name='fornecedores'),
    path('fornecedores/adicionar/', FornecedorAdicionarView.as_view(), name='adicionar_fornecedor'),

    # Clientes
    path('clientes/', ClienteView.as_view(), name='clientes'),
    path('clientes/adicionar/', ClienteAdicionarView.as_view(), name='adicionar_cliente'),

    # Cidades
    path('cidades/', CidadeView.as_view(), name='cidades'),
    path('cidades/adicionar/', CidadeAdicionarView.as_view(), name='adicionar_cidade'),

    # Unidades federativas
    path('ufs/', UFView.as_view(), name='ufs'),
    path('ufs/adicionar/', UFAdicionarView.as_view(), name='adicionar_uf'),

    # Vendas
    path('vendas/', VendaView.as_view(), name='vendas'),
    path('vendas/adicionar/', VendaAdicionarView.as_view(), name='adicionar_venda'),

    # Itens de venda
    path('itens-vendas/', ItemVendaView.as_view(), name='itens_vendas'),
    path('itens-vendas/adicionar/', ItemVendaAdicionarView.as_view(), name='adicionar_item_venda'),

    # Estoque
    path('estoques/', EstoqueView.as_view(), name='estoques'),
    path('estoques/adicionar/', EstoqueAdicionarView.as_view(), name='adicionar_estoque'),

    # Entradas de produtos
    path('entradas-produtos/', EntradaProdutoView.as_view(), name='entradas_produtos'),
    path('entradas-produtos/adicionar/', EntradaProdutoAdicionarView.as_view(), name='adicionar_entrada'),

    # Pedras
    path('pedras/', PedraView.as_view(), name='pedras'),
    path('pedras/adicionar/', PedraAdicionarView.as_view(), name='adicionar_pedra'),
]
