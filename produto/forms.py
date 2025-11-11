from django import forms 
from fornecedor.querys import get_id_nome_fornecedor
from categoria.querys import get_id_nome_by_categoria  # importante
ID_E_NOME_FORNECEDOR = get_id_nome_fornecedor()
from . import querys

class ProdutoForm(forms.Form):
    nome_produto = forms.CharField(max_length=100)
    preco_venda = forms.DecimalField(max_digits=19, decimal_places=4)
    preco_custo = forms.DecimalField(max_digits=19, decimal_places=4)
    quantidade = forms.IntegerField(min_value=0)
    id_fornecedor = forms.ChoiceField(choices = [], 
    widget=forms.Select(attrs={'class': 'form-control'}))
    id_categoria = forms.ChoiceField(choices = [],
    widget = forms.Select(attrs={'class': 'form-control'}))
    

    def __init__(self, *args, **kwargs):
        self.id_produto = kwargs.pop('id_produto', None)
        super().__init__(*args, **kwargs)
        self.fields['id_fornecedor'].choices = get_id_nome_fornecedor()
        self.fields['id_categoria'].choices = get_id_nome_by_categoria()
    
    def clean_nome_produto(self):
            nome_produto = self.cleaned_data['nome_produto']
    
            if not self.id_produto:
                if querys.get_produto_by_nome(nome_produto):
                    raise forms.ValidationError("Já existe um produto com esse nome.")
            else:
                produto_atual = querys.get_produto_by_id(self.id_produto)
                nome_atual = produto_atual[1] if produto_atual else None
    
                if nome_produto != nome_atual and querys.get_produto_by_nome(nome_produto):
                    raise forms.ValidationError("Já existe um produto com esse nome.")
            
            return nome_produto