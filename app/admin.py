
from django.contrib import admin
from .models import *

# i) Tipos de produtos e produtos
class ProdutoTipoInline(admin.TabularInline):
    model = Produto
    extra = 1


@admin.register(TipoProduto)
class TipoProdutoAdmin(admin.ModelAdmin):
    inlines = [ProdutoTipoInline]


# ii) Materiais e produtos
class ProdutoMaterialInline(admin.TabularInline):
    model = Produto
    extra = 1


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    inlines = [ProdutoMaterialInline]


# iii) Produtos e pedras
class ProdutoPedraInline(admin.TabularInline):
    model = Produto.pedras.through
    extra = 1


@admin.register(Pedra)
class PedraAdmin(admin.ModelAdmin):
    inlines = [ProdutoPedraInline]


# iv) Produtos e entradas de produtos
class EntradaProdutoInline(admin.TabularInline):
    model = EntradaProduto
    extra = 1


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    inlines = [EntradaProdutoInline]


# v) Vendas e itens de venda
class ItemVendaInline(admin.TabularInline):
    model = ItemVenda
    extra = 1


@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    inlines = [ItemVendaInline]


# vi) Clientes e vendas
class VendaClienteInline(admin.TabularInline):
    model = Venda
    extra = 1


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    inlines = [VendaClienteInline]


# vii) Fornecedores e entradas de produtos
class EntradaFornecedorInline(admin.TabularInline):
    model = EntradaProduto
    extra = 1


@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    inlines = [EntradaFornecedorInline]


# viii) UF e cidades
class CidadeInline(admin.TabularInline):
    model = Cidade
    extra = 1


@admin.register(UF)
class UFAdmin(admin.ModelAdmin):
    inlines = [CidadeInline]


# ix) Cidades
admin.site.register(Cidade)


# x) Estoque
admin.site.register(Estoque)
