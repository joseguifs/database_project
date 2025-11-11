from django.shortcuts import render, redirect
from django.views import View
from . import querys
from .forms import ProdutoForm
from fornecedor.querys import get_nome_fornecedor_by_id
from categoria.querys import get_nome_categoria_by_id
from fornecedor.forms import ID_E_NOME_CATEGORIA
from .forms import ID_E_NOME_FORNECEDOR

class Produto:
    def __init__(self, id_produto, nome_produto, preco_venda, preco_custo, quantidade, fornecedor, categoria):
        self.id_produto = id_produto
        self.nome_produto = nome_produto
        self.preco_venda = preco_venda 
        self.preco_custo = preco_custo
        self.quantidade = quantidade
        self.fornecedor = fornecedor
        self.categoria = categoria
        

class ProdutoGetView(View):
    def get(self, request, *args, **kwargs):
        produtos_raw = querys.get_produtos()
        nomes_fornecedores = [get_nome_fornecedor_by_id(item[5]) for item in produtos_raw]
        nomes_categorias = [get_nome_categoria_by_id(item[6]) for item in produtos_raw]

        produtos = []
        for produto_raw, nome_fornecedor, nome_categoria in zip(produtos_raw, nomes_fornecedores, nomes_categorias):
            produtos.append(
                Produto(
                    produto_raw[0],  
                    produto_raw[1],  
                    produto_raw[2],  
                    produto_raw[3],  
                    produto_raw[4],  
                    nome_fornecedor,
                    nome_categoria
                )
            )

        return render(request, 'produto.html', {'produtos': produtos})

        
class ProdutoGetByIdView(View):
    def get(self, request, id, *args, **kwargs):
        contexto = False
        produto = querys.get_produto_by_id(id)
        
        if produto:
            id_fornecedor = produto[5]  
            id_categoria = produto[6]
            nome_fornecedor_produto = get_nome_fornecedor_by_id(id_fornecedor)
            nome_categoria_produto = get_nome_categoria_by_id(id_categoria)
            contexto = Produto(produto[0], produto[1], produto[2], produto[3], produto[4], nome_fornecedor_produto, nome_categoria_produto)
        return render(request, 'produto_read.html', {'produto': contexto})
        
class ProdutoPostView(View):
    def get(self, request, *args, **kwargs):
        form = ProdutoForm()
        return render(request, 'produto_post.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ProdutoForm(request.POST)
        if form.is_valid():
            querys.post_produto(form.cleaned_data['nome_produto'], form.cleaned_data['preco_venda'], form.cleaned_data['preco_custo'], form.cleaned_data['quantidade'], form.cleaned_data['id_fornecedor'], form.cleaned_data['id_categoria'])
            return redirect('produtos')
        return render(request, 'produto_post.html', {'form': form})

class ProdutoPutView(View):
    def get(self, request, id, *args, **kwargs):
        produto = querys.get_produto_by_id(id)
        if not produto:
           return render(request, 'produto_put.html', {'form': False})
        
        form = ProdutoForm(initial={'nome_produto': produto[1], 'preco_venda': produto[2], 'preco_custo': produto[3], 'quantidade': produto[4], 'id_fornecedor': produto[5], 'id_categoria': produto[6]}, id_produto=id)
        form.fields['id_fornecedor'].choices = ID_E_NOME_FORNECEDOR
        form.fields['id_categoria'].choices = ID_E_NOME_CATEGORIA
        
        return render(request, 'produto_put.html', {'form':form})
    
    
    def post(self, request, id, *args, **kwargs):
        form = ProdutoForm(request.POST, id_produto=id)
        if form.is_valid():
            querys.put_produto(id, form.cleaned_data['nome_produto'], form.cleaned_data['preco_venda'], form.cleaned_data['preco_custo'], form.cleaned_data['quantidade'], form.cleaned_data['id_fornecedor'], form.cleaned_data['id_categoria'])
            return redirect('produtos')
        return render(request, 'produto_put.html', {'form': form})
        
class ProdutoDeleteView(View):
    def get(self, request, id, *args, **kwargs):
        contexto = False
        produto = querys.get_produto_by_id(id)
        if produto:
            id_fornecedor = produto[5] 
            id_categoria = produto[6]
            nome_fornecedor_produto = get_nome_fornecedor_by_id(id_fornecedor)
            nome_categoria_produto = get_nome_categoria_by_id(id_categoria)
            contexto = Produto(produto[0], produto[1], produto[2], produto[3], produto[4], nome_fornecedor_produto, nome_categoria_produto)
        return render(request, 'produto_delete.html', {'produto': contexto})
    
    def post(self, request, id, *args, **kwargs):
        querys.delete_produto(id)
        return redirect('produtos')
