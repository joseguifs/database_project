from django import forms
from . import querys


class CategoriaForm(forms.Form):
    nome = forms.CharField(max_length=30)
    descricao = forms.CharField(widget=forms.Textarea, max_length=100)
    
    def clean_nome(self):
        nome = self.cleaned_data['nome']
        if querys.get_categoria_by_nome(nome):
            raise forms.ValidationError('Já existe uma categoria com esse nome.')
        return nome
    