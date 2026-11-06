from django.db import models

# Create your models here.

# RF07 - Gerenciar unidades federativas
class UF(models.Model):
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=2)

    def __str__(self):
        return self.sigla


# RF06 - Gerenciar cidades
class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    uf = models.ForeignKey(UF, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome


# RF02 - Gerenciar tipos de produtos
class TipoProduto(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


# RF03 - Gerenciar materiais
class Material(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


# RF12 - Gerenciar pedras
class Pedra(models.Model):
    nome = models.CharField(max_length=100)
    cor = models.CharField(max_length=50)
    tipo = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


# RF01 - Gerenciar produtos
class Produto(models.Model):
    nome = models.CharField(max_length=150)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.PositiveIntegerField(default=0)
    descricao = models.TextField(blank=True, null=True)
    possui_pedra = models.BooleanField(default=False)

    tipo = models.ForeignKey(
        TipoProduto,
        on_delete=models.PROTECT
    )

    material = models.ForeignKey(
        Material,
        on_delete=models.PROTECT
    )

    pedras = models.ManyToManyField(
        Pedra,
        blank=True
    )

    tamanho_anel = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    comprimento_cm = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.nome


# RF04 - Gerenciar fornecedores
class Fornecedor(models.Model):
    nome = models.CharField(max_length=150)
    cnpj = models.CharField(max_length=18, unique=True)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=200)
    cidade = models.ForeignKey(
        Cidade,
        on_delete=models.PROTECT
    )

    def __str__(self):
        return self.nome


# RF05 - Gerenciar clientes
class Cliente(models.Model):
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=14, unique=True)
    data_nasc = models.DateField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=200)
    cidade = models.ForeignKey(
        Cidade,
        on_delete=models.PROTECT
    )

    def __str__(self):
        return self.nome


# RF08 - Gerenciar vendas
class Venda(models.Model):
    data_venda = models.DateTimeField(auto_now_add=True)
    valor_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.PROTECT
    )

    def __str__(self):
        return f"Venda {self.id}"


# RF09 - Gerenciar itens de venda
class ItemVenda(models.Model):
    venda = models.ForeignKey(
        Venda,
        on_delete=models.CASCADE,
        related_name="itens"
    )

    produto = models.ForeignKey(
        Produto,
        on_delete=models.PROTECT
    )

    quantidade = models.PositiveIntegerField()
    valor_unitario = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):
        return f"{self.produto.nome} - {self.quantidade}"


# RF11 - Gerenciar entradas de produtos
class EntradaProduto(models.Model):
    produto = models.ForeignKey(
        Produto,
        on_delete=models.PROTECT
    )

    fornecedor = models.ForeignKey(
        Fornecedor,
        on_delete=models.PROTECT
    )

    quantidade = models.PositiveIntegerField()
    data_entrada = models.DateField(auto_now_add=True)

    valor_compra = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):
        return f"Entrada - {self.produto.nome}"


# RF10 - Gerenciar estoque
class Estoque(models.Model):
    produto = models.OneToOneField(
        Produto,
        on_delete=models.CASCADE
    )

    quantidade_atual = models.PositiveIntegerField(default=0)
    quantidade_minima = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.produto.nome
