from django import forms
from . import querys

class CategoriaForm(forms.Form):
    nome = forms.CharField(max_length=30)
    descricao = forms.CharField(widget=forms.Textarea, max_length=100)

    def __init__(self, *args, **kwargs):
        # Captura o ID da categoria atual (caso estejamos editando)
        self.id_categoria = kwargs.pop('id_categoria', None)
        super().__init__(*args, **kwargs)

    def clean_nome(self):
        nome = self.cleaned_data['nome']

        if not self.id_categoria:
            # Caso seja criação de nova categoria
            if querys.get_categoria_by_nome(nome):
                raise forms.ValidationError('Já existe uma categoria com esse nome.')
        else:
            # Caso seja atualização
            categoria_atual = querys.get_categoria_by_id(self.id_categoria)
            nome_atual = categoria_atual[1] if categoria_atual else None

            # Se o nome foi alterado e já existe outro igual
            if nome != nome_atual and querys.get_categoria_by_nome(nome):
                raise forms.ValidationError('Já existe uma categoria com esse nome.')

        return nome
