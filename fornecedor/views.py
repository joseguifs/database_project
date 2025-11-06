from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection


# Create your views here.
def teste(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM FORNECEDORES LIMIT 0;")
        colunas = [desc[0] + " " for desc in cursor.description]
        return HttpResponse(colunas)