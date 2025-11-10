from django import forms
from categoria import querys as categoria_querys
from . import querys

ID_E_NOME_CATEGORIA = categoria_querys.get_id_nome_by_categoria()

class FornecedorForm(forms.Form):
    nome_fornecedor = forms.CharField(max_length=100)
    descricao = forms.CharField(max_length=200)
    telefone = forms.CharField(max_length=20)
    cidade = forms.CharField(max_length=100)
    estado = forms.CharField(max_length=100)
    created_at = forms.DateField()
    id_categoria = forms.MultipleChoiceField(choices = ID_E_NOME_CATEGORIA,
    widget = forms.SelectMultiple(attrs={'class': 'form-control'}))
    
    def __init__(self, *args, **kwargs):
        # Recebe o id do fornecedor (somente na edição)
        self.id_fornecedor = kwargs.pop('id_fornecedor', None)
        super().__init__(*args, **kwargs)
    
    def clean_nome_fornecedor(self):
        nome_fornecedor = self.cleaned_data['nome_fornecedor']
        if querys.get_fornecedor_by_nome(nome_fornecedor) and not self.id_fornecedor:
            raise forms.ValidationError('Já existe um fornecedor com esse nome.')
        return nome_fornecedor

        
    
    