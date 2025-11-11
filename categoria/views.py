from django.shortcuts import render, redirect
from django.views import View
from .forms import CategoriaForm
from . import querys

class Categoria:
    def __init__(self, id, nome, descricao):
        self.id = id
        self.nome = nome
        self.descricao = descricao

class CategoriaGetView(View):
    def get(self, request, *args, **kwargs):
        categorias_raw = querys.get_categorias()
        categorias = [
                Categoria(item[0], item[1], item[2])
                for item in categorias_raw
            ]
        return render(request, 'categoria.html', {'categorias': categorias})
        
class CategoriaGetByIdView(View):
    def get(self, request, id, *args, **kwargs):
        contexto = False
        categoria = querys.get_categoria_by_id(id)
        if categoria:
            contexto = Categoria(categoria[0], categoria[1], categoria[2])
        return render(request, 'categoria_read.html', {'categoria': contexto})
        
class CategoriaPostView(View):
    def get(self, request, *args, **kwargs):
        form = CategoriaForm()
        return render(request, 'categoria_post.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = CategoriaForm(request.POST)
        if form.is_valid():
            querys.post_categoria(form.cleaned_data['nome'], form.cleaned_data['descricao'])
            return redirect('categorias')
        return render(request, 'categoria_post.html', {'form': form})

class CategoriaPutView(View):
    def get(self, request, id, *args, **kwargs):
        categoria = querys.get_categoria_by_id(id)
        if not categoria:
            return render(request, 'categoria_put.html', {'form': False}) 

        form = CategoriaForm(initial={
            'nome': categoria[1],
            'descricao': categoria[2]
        }, id_categoria=id)
        return render(request, 'categoria_put.html', {'form': form})
    
    def post(self, request, id, *args, **kwargs):
        form = CategoriaForm(request.POST, id_categoria=id)
        if form.is_valid():
            querys.put_categoria(
                id,
                form.cleaned_data['nome'],
                form.cleaned_data['descricao']
            )
            return redirect('categorias')
        return render(request, 'categoria_put.html', {'form': form})

        
class CategoriaDeleteView(View):
    def get(self, request, id, *args, **kwargs):
        contexto = False
        categoria = querys.get_categoria_by_id(id)
        if categoria:
            contexto = Categoria(categoria[0], categoria[1], categoria[2])
        return render(request, 'categoria_delete.html', {'categoria': contexto})
    
    def post(self, request, id, *args, **kwargs):
        querys.delete_categoria(id)
        return redirect('categorias')
