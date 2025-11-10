from multiprocessing.reduction import register
from django.db import connection

def get_fornecedores():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM fornecedores")
        return cursor.fetchall()
    
def get_fornecedor_by_id(id):
    with connection.cursor() as cursor:
        raw = cursor.execute("SELECT * FROM fornecedores WHERE id_fornecedor = %s", [id])
        if raw == 0:
            return False
        return cursor.fetchone()

def get_specific_id_nome_by_categoria(lista_id:list):
    categorias = []
    with connection.cursor() as cursor:
        for id in lista_id:
            cursor.execute("SELECT nome_categoria FROM categoria WHERE id_categoria = %s", [id])
            resultado = cursor.fetchone()
            if resultado:
                categorias.append((id, resultado[0]))
    return categorias

def get_fornecedor_by_nome(nome):
    with connection.cursor() as cursor:
        raw = cursor.execute("SELECT * FROM fornecedores WHERE nome_fornecedor = %s", [nome])
        if raw > 0:
            return True
        return False

def post_fornecedor(nome, descricao, telefone, cidade, estado, created_at):
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO fornecedores (nome_fornecedor, descricao, telefone, cidade, estado, created_at) VALUES (%s, %s, %s, %s, %s, %s)", [nome, descricao, telefone, cidade, estado, created_at])
        return cursor.lastrowid
        
def get_fornecedor_categoria(id_fornecedor):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM fornecedor_categoria WHERE id_fornecedor = %s", [id_fornecedor])
        return cursor.fetchall()

def get_categorianame_for_fornecedor(id_fornecedor):
    with connection.cursor() as cursor:
        cursor.execute("SELECT nome_categoria FROM categoria INNER JOIN fornecedor_categoria ON categoria.id_categoria = fornecedor_categoria.id_categoria WHERE fornecedor_categoria.id_fornecedor = %s", [id_fornecedor])
        return cursor.fetchall()

def get_id_categoria_fornecedor_categoria(id_fornecedor):
    with connection.cursor() as cursor:
        cursor.execute("SELECT id_categoria FROM fornecedor_categoria WHERE id_fornecedor = %s", [id_fornecedor])
        return cursor.fetchall()

def post_fornecedor_categoria(id_fornecedor, id_categoria):
    num_categorias = len(id_categoria) > 1
    if num_categorias:
        for id in id_categoria:
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO fornecedor_categoria (id_fornecedor, id_categoria) VALUES (%s, %s)", [id_fornecedor, id])
        return
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO fornecedor_categoria (id_fornecedor, id_categoria) VALUES (%s, %s)", [id_fornecedor, id_categoria[0]])

def put_fornecedor(id, nome, descricao, telefone, cidade, estado):
    with connection.cursor() as cursor:
        cursor.execute("UPDATE fornecedores SET nome_fornecedor = %s, descricao = %s, telefone = %s, cidade = %s, estado = %s WHERE id_fornecedor = %s", [nome, descricao, telefone, cidade, estado, id])

def put_fornecedor_categoria(id_fornecedor, id_categoria):
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT id_categoria FROM fornecedor_categoria WHERE id_fornecedor = %s",
            [id_fornecedor]
        )
        registros = cursor.fetchall()

    ids_antigos = {int(registro[0]) for registro in registros}
    ids_atuais = {int(cat_id) for cat_id in id_categoria}

    adicionados = ids_atuais - ids_antigos
    removidos = ids_antigos - ids_atuais

    if adicionados:
        with connection.cursor() as cursor:
            for id_cat in adicionados:
                cursor.execute(
                    "INSERT INTO fornecedor_categoria (id_fornecedor, id_categoria) VALUES (%s, %s)",
                    [id_fornecedor, id_cat]
                )

    if removidos:
        with connection.cursor() as cursor:
            for id_cat in removidos:
                cursor.execute(
                    "DELETE FROM fornecedor_categoria WHERE id_fornecedor = %s AND id_categoria = %s",
                    [id_fornecedor, id_cat]
                )


def delete_fornecedor(id):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM fornecedor_categoria WHERE id_fornecedor = %s", [id])
        cursor.execute("DELETE FROM fornecedores WHERE id_fornecedor = %s", [id])
