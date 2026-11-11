from django.shortcuts import render

from django.views import View
from .models import *


# RF01 - Gerenciar produtos
class ProdutoView(View):
    def get(self, request, *args, **kwargs):
        dados = Produto.objects.all()
        return render(request, 'produtos.html', {'dados': dados})


# RF02 - Gerenciar tipos de produtos
class TipoProdutoView(View):
    def get(self, request, *args, **kwargs):
        dados = TipoProduto.objects.all()
        return render(request, 'tipos_produtos.html', {'dados': dados})


# RF03 - Gerenciar materiais
class MaterialView(View):
    def get(self, request, *args, **kwargs):
        dados = Material.objects.all()
        return render(request, 'materiais.html', {'dados': dados})


# RF04 - Gerenciar fornecedores
class FornecedorView(View):
    def get(self, request, *args, **kwargs):
        dados = Fornecedor.objects.all()
        return render(request, 'fornecedores.html', {'dados': dados})


# RF05 - Gerenciar clientes
class ClienteView(View):
    def get(self, request, *args, **kwargs):
        dados = Cliente.objects.all()
        return render(request, 'clientes.html', {'dados': dados})


# RF06 - Gerenciar cidades
class CidadeView(View):
    def get(self, request, *args, **kwargs):
        dados = Cidade.objects.all()
        return render(request, 'cidades.html', {'dados': dados})


# RF07 - Gerenciar unidades federativas
class UFView(View):
    def get(self, request, *args, **kwargs):
        dados = UF.objects.all()
        return render(request, 'ufs.html', {'dados': dados})


# RF08 - Gerenciar vendas
class VendaView(View):
    def get(self, request, *args, **kwargs):
        dados = Venda.objects.all()
        return render(request, 'vendas.html', {'dados': dados})


# RF09 - Gerenciar itens de venda
class ItemVendaView(View):
    def get(self, request, *args, **kwargs):
        dados = ItemVenda.objects.all()
        return render(request, 'itens_venda.html', {'dados': dados})


# RF10 - Gerenciar estoque
class EstoqueView(View):
    def get(self, request, *args, **kwargs):
        dados = Estoque.objects.all()
        return render(request, 'estoques.html', {'dados': dados})


# RF11 - Gerenciar entradas de produtos
class EntradaProdutoView(View):
    def get(self, request, *args, **kwargs):
        dados = EntradaProduto.objects.all()
        return render(request, 'entradas_produtos.html', {'dados': dados})


# RF12 - Gerenciar pedras
class PedraView(View):
    def get(self, request, *args, **kwargs):
        dados = Pedra.objects.all()
        return render(request, 'pedras.html', {'dados': dados})


# RF13 - Gerenciar produtos com pedras
class ProdutoPedraView(View):
    def get(self, request, *args, **kwargs):
        dados = Produto.objects.prefetch_related('pedras').all()
        return render(request, 'produtos_pedras.html', {'dados': dados})


# Página inicial
class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
