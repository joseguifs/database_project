from django.shortcuts import render, redirect
from django.views import View
from . import querys
from .forms import FornecedorForm, ID_E_NOME_CATEGORIA 

# TODO: Implementar as classes que estão faltando e ajeitar as classes no urls.py 
# TODO: Corrigir as queries de fornecedor

class Fornecedor:
    def __init__(self, id_fornecedor, nome_fornecedor, descricao, telefone, cidade, estado, created_at):
        self.id_fornecedor = id_fornecedor
        self.nome_fornecedor = nome_fornecedor
        self.descricao = descricao
        self.telefone = telefone
        self.cidade = cidade
        self.estado = estado
        self.created_at = created_at
        self.categoria = []

class FornecedorGetView(View):
    def get(self, request, *args, **kwargs):
        fornecedores_raw = querys.get_fornecedores()
        fornecedores = [
                Fornecedor(item[0], item[1], item[2], item[3], item[4], item[5], item[6])
                for item in fornecedores_raw
            ]
        return render(request, 'fornecedor.html', {'fornecedores': fornecedores})
        
class FornecedorGetByIdView(View):
    def get(self, request, id, *args, **kwargs):
        contexto = False
        fornecedor = querys.get_fornecedor_by_id(id)
        if fornecedor:
            categoria = [raw[0] for raw in querys.get_categorianame_for_fornecedor(id)]
            contexto = Fornecedor(fornecedor[0], fornecedor[1], fornecedor[2], fornecedor[3], fornecedor[4], fornecedor[5], fornecedor[6])
            contexto.categoria.extend(categoria)
        return render(request, 'fornecedor_read.html', {'fornecedor': contexto})
        
class FornecedorPostView(View):
    def get(self, request, *args, **kwargs):
        form = FornecedorForm()
        return render(request, 'fornecedor_post.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = FornecedorForm(request.POST)
        if form.is_valid():
            id_fornecedor = querys.post_fornecedor(form.cleaned_data['nome_fornecedor'], form.cleaned_data['descricao'], form.cleaned_data['telefone'], form.cleaned_data['cidade'], form.cleaned_data['estado'], form.cleaned_data['created_at'])
            querys.post_fornecedor_categoria(id_fornecedor, form.cleaned_data['id_categoria'])
            return redirect('categorias')
        return render(request, 'fornecedor_post.html', {'form': form})

class FornecedorPutView(View):
    def get(self, request, id, *args, **kwargs):
        fornecedor = querys.get_fornecedor_by_id(id)
        if not fornecedor:
           return render(request, 'fornecedor_put.html', {'form': False})
        lista_id = querys.get_id_categoria_fornecedor_categoria(id)
        form = FornecedorForm(initial={'nome_fornecedor': fornecedor[1], 'descricao': fornecedor[2], 'telefone': fornecedor[3], 'cidade': fornecedor[4], 'estado': fornecedor[5], 'created_at': fornecedor[6], 'id_categoria': lista_id},id_fornecedor=id)
        form.fields['id_categoria'].choices = ID_E_NOME_CATEGORIA
        return render(request, 'fornecedor_put.html', {'form':form})
    
    
    def post(self, request, id, *args, **kwargs):
        form = FornecedorForm(request.POST, id_fornecedor=id)
        if form.is_valid():
            querys.put_fornecedor(id, form.cleaned_data['nome_fornecedor'], form.cleaned_data['descricao'], form.cleaned_data['telefone'], form.cleaned_data['cidade'], form.cleaned_data['estado'])
            querys.put_fornecedor_categoria(id, form.cleaned_data['id_categoria'])
            
            return redirect('fornecedores')
        return render(request, 'fornecedor_put.html', {'form': form})
        
class FornecedorDeleteView(View):
    def get(self, request, id, *args, **kwargs):
        contexto = False
        fornecedor = querys.get_fornecedor_by_id(id)
        if fornecedor:
            categoria = [raw[0] for raw in querys.get_categorianame_for_fornecedor(id)]
            contexto = Fornecedor(fornecedor[0], fornecedor[1], fornecedor[2], fornecedor[3], fornecedor[4], fornecedor[5], fornecedor[6])
            contexto.categoria.extend(categoria)
        return render(request, 'fornecedor_delete.html', {'fornecedor': contexto})
    
    def post(self, request, id, *args, **kwargs):
        querys.delete_fornecedor(id)
        return redirect('fornecedores')
