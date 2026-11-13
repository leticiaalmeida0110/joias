
from django import forms
from .models import *


# RF01 - Produtos
class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = [
            'nome', 'valor', 'quantidade', 'descricao',
            'possui_pedra', 'tipo', 'material', 'pedras',
            'tamanho_anel', 'comprimento_cm'
        ]

        labels = {
            'nome': 'Nome',
            'valor': 'Valor (R$)',
            'quantidade': 'Quantidade',
            'descricao': 'Descrição',
            'possui_pedra': 'Possui pedra',
            'tipo': 'Tipo',
            'material': 'Material',
            'pedras': 'Pedras',
            'tamanho_anel': 'Tamanho do anel',
            'comprimento_cm': 'Comprimento (cm)',
        }

        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 4}),
            'pedras': forms.CheckboxSelectMultiple(),
        }


# RF02 - Tipos de produtos
class TipoProdutoForm(forms.ModelForm):
    class Meta:
        model = TipoProduto
        fields = ['nome']
        labels = {'nome': 'Nome do tipo'}


# RF03 - Materiais
class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['nome']
        labels = {'nome': 'Nome do material'}


# RF04 - Fornecedores
class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = [
            'nome', 'cnpj', 'email',
            'telefone', 'endereco', 'cidade'
        ]


# RF05 - Clientes
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'nome', 'cpf', 'data_nasc',
            'email', 'telefone', 'endereco', 'cidade'
        ]

        widgets = {
            'data_nasc': forms.DateInput(attrs={'type': 'date'}),
        }


# RF06 - Cidades
class CidadeForm(forms.ModelForm):
    class Meta:
        model = Cidade
        fields = ['nome', 'uf']
        labels = {
            'nome': 'Nome da cidade',
            'uf': 'Unidade federativa',
        }


# RF07 - Unidades federativas
class UFForm(forms.ModelForm):
    class Meta:
        model = UF
        fields = ['nome', 'sigla']
        labels = {
            'nome': 'Nome do estado',
            'sigla': 'Sigla',
        }


# RF08 - Vendas
class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ['cliente', 'valor_total']
        labels = {
            'cliente': 'Cliente',
            'valor_total': 'Valor total (R$)',
        }


# RF09 - Itens de venda
class ItemVendaForm(forms.ModelForm):
    class Meta:
        model = ItemVenda
        fields = [
            'venda', 'produto',
            'quantidade', 'valor_unitario'
        ]


# RF10 - Estoque
class EstoqueForm(forms.ModelForm):
    class Meta:
        model = Estoque
        fields = [
            'produto', 'quantidade_atual',
            'quantidade_minima'
        ]


# RF11 - Entradas de produtos
class EntradaProdutoForm(forms.ModelForm):
    class Meta:
        model = EntradaProduto
        fields = [
            'produto', 'fornecedor',
            'quantidade', 'valor_compra'
        ]


# RF12 - Pedras
class PedraForm(forms.ModelForm):
    class Meta:
        model = Pedra
        fields = ['nome', 'cor', 'tipo']
        labels = {
            'nome': 'Nome da pedra',
            'cor': 'Cor',
            'tipo': 'Tipo da pedra',
        }
