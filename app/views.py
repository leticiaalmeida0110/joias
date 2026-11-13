from django.shortcuts import render

from django.views import View
from .models import *
from django.shortcuts import render, redirect
from .forms import ProdutoForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import *

# RF01 - Gerenciar produtos
class ProdutoView(View):
    def get(self, request, *args, **kwargs):
        dados = Produto.objects.all()
        return render(request, 'produtos.html', {'dados': dados})


# RF01 - Adicionar produtos
class ProdutoAdicionarView(View):

    def get(self, request, *args, **kwargs):
        form = ProdutoForm()
        return render(request, 'adicionar_produto.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ProdutoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('produtos')

        return render(request, 'adicionar_produto.html', {'form': form})

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
    

# Classe base para os cadastros
class CadastroBaseView(CreateView):
    template_name = 'formulario.html'


# RF02 - Adicionar tipos de produtos
class TipoProdutoAdicionarView(CadastroBaseView):
    model = TipoProduto
    form_class = TipoProdutoForm
    success_url = reverse_lazy('tipos_produtos')
    extra_context = {'titulo': 'Adicionar tipo de produto'}


# RF03 - Adicionar materiais
class MaterialAdicionarView(CadastroBaseView):
    model = Material
    form_class = MaterialForm
    success_url = reverse_lazy('materiais')
    extra_context = {'titulo': 'Adicionar material'}


# RF04 - Adicionar fornecedores
class FornecedorAdicionarView(CadastroBaseView):
    model = Fornecedor
    form_class = FornecedorForm
    success_url = reverse_lazy('fornecedores')
    extra_context = {'titulo': 'Adicionar fornecedor'}


# RF05 - Adicionar clientes
class ClienteAdicionarView(CadastroBaseView):
    model = Cliente
    form_class = ClienteForm
    success_url = reverse_lazy('clientes')
    extra_context = {'titulo': 'Adicionar cliente'}


# RF06 - Adicionar cidades
class CidadeAdicionarView(CadastroBaseView):
    model = Cidade
    form_class = CidadeForm
    success_url = reverse_lazy('cidades')
    extra_context = {'titulo': 'Adicionar cidade'}


# RF07 - Adicionar unidades federativas
class UFAdicionarView(CadastroBaseView):
    model = UF
    form_class = UFForm
    success_url = reverse_lazy('ufs')
    extra_context = {'titulo': 'Adicionar unidade federativa'}


# RF08 - Adicionar vendas
class VendaAdicionarView(CadastroBaseView):
    model = Venda
    form_class = VendaForm
    success_url = reverse_lazy('vendas')
    extra_context = {'titulo': 'Registrar venda'}


# RF09 - Adicionar itens de venda
class ItemVendaAdicionarView(CadastroBaseView):
    model = ItemVenda
    form_class = ItemVendaForm
    success_url = reverse_lazy('itens_vendas')
    extra_context = {'titulo': 'Adicionar item de venda'}


# RF10 - Adicionar estoque
class EstoqueAdicionarView(CadastroBaseView):
    model = Estoque
    form_class = EstoqueForm
    success_url = reverse_lazy('estoques')
    extra_context = {'titulo': 'Cadastrar estoque'}


# RF11 - Adicionar entradas de produtos
class EntradaProdutoAdicionarView(CadastroBaseView):
    model = EntradaProduto
    form_class = EntradaProdutoForm
    success_url = reverse_lazy('entradas_produtos')
    extra_context = {'titulo': 'Registrar entrada de produto'}


# RF12 - Adicionar pedras
class PedraAdicionarView(CadastroBaseView):
    model = Pedra
    form_class = PedraForm
    success_url = reverse_lazy('pedras')
    extra_context = {'titulo': 'Adicionar pedra'}

