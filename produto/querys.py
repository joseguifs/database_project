from multiprocessing.reduction import register
from django.db import connection
from decimal import Decimal, InvalidOperation

def normalizar_decimal(valor):
    if isinstance(valor, (int, float, Decimal)):
        return Decimal(str(valor))
    if isinstance(valor, str):
        valor = valor.strip().replace(' ', '')
        # Substitui vírgula por ponto, mas mantém apenas o último ponto como separador decimal
        valor = valor.replace('.', '').replace(',', '.')
        try:
            return Decimal(valor)
        except InvalidOperation:
            return Decimal('0.00')
    return Decimal('0.00')

def get_produtos():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM produto")
        return cursor.fetchall()
    
def get_produto_by_id(id):
    with connection.cursor() as cursor:
        raw = cursor.execute("SELECT * FROM produto WHERE id_produto = %s", [id])
        if raw == 0:
            return False
        return cursor.fetchone()
        
def get_id_nome_fornecedor():
    with connection.cursor() as cursor:
        cursor.execute("SELECT id_fornecedor, nome_fornecedor FROM fornecedores")
        return cursor.fetchall()


def get_produto_by_nome(nome):
    with connection.cursor() as cursor:
        raw = cursor.execute("SELECT * FROM produto WHERE nome_produto = %s", [nome])
        if raw > 0:
            return True
        return False

def post_produto(nome, preco_venda, preco_custo, quantidade, id_fornecedor, id_categoria):
    preco_venda = normalizar_decimal(preco_venda)
    preco_custo = normalizar_decimal(preco_custo)
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO produto (nome_produto, preco_venda, preco_custo, quantidade, id_fornecedor, id_categoria) VALUES (%s, %s, %s, %s, %s, %s)", [nome, preco_venda, preco_custo, quantidade, id_fornecedor, id_categoria])

                
def put_produto(id_produto, nome_produto, preco_venda, preco_custo, quantidade, id_fornecedor, id_categoria):
    preco_venda = normalizar_decimal(preco_venda)
    preco_custo = normalizar_decimal(preco_custo)
    with connection.cursor() as cursor:
        cursor.execute(
            "UPDATE produto SET nome_produto = %s, preco_venda = %s, preco_custo = %s, quantidade = %s, id_fornecedor = %s, id_categoria = %s WHERE id_produto = %s",
            [nome_produto, preco_venda, preco_custo, quantidade, id_fornecedor, id_categoria, id_produto]
        )

def delete_produto(id):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM produto WHERE id_produto = %s", [id])