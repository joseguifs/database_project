from django.db import connection

def get_categorias():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM categoria")
        return cursor.fetchall()
    
def get_categoria_by_id(id):
    with connection.cursor() as cursor:
        raw = cursor.execute("SELECT * FROM categoria WHERE id_categoria = %s", [id])
        if raw == 0:
            return False
        return cursor.fetchone()

def get_categoria_by_nome(nome):
    with connection.cursor() as cursor:
        raw = cursor.execute("SELECT * FROM categoria WHERE nome_categoria = %s", [nome])
        if raw > 0:
            return True
        return False

def get_id_nome_by_categoria():
    with connection.cursor() as cursor:
        cursor.execute("SELECT id_categoria, nome_categoria FROM categoria")
        return cursor.fetchall()

def post_categoria(nome, descricao):
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO categoria (nome_categoria, descricao) VALUES (%s, %s)", [nome, descricao])

def put_categoria(id, nome, descricao):
    with connection.cursor() as cursor:
        cursor.execute("UPDATE categoria SET nome_categoria = %s, descricao = %s WHERE id_categoria = %s", [nome, descricao, id])

def delete_categoria(id):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM categoria WHERE id_categoria = %s", [id])
