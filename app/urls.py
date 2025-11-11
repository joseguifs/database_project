"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

from categoria import views
from fornecedor import views as fornecedor_views

from produto import views as produto_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("categoria/", views.CategoriaGetView.as_view(), name="categorias"),
    path("categoria/<int:id>/",views.CategoriaGetByIdView.as_view(),name="categoria_detail",),
    path("categoria/create/", views.CategoriaPostView.as_view(), name="categoria_create"),
    path("categoria/update/<int:id>/",views.CategoriaPutView.as_view(),name="categoria_update"),
    path("categoria/delete/<int:id>/",views.CategoriaDeleteView.as_view(),name="categoria_delete"),
    path("fornecedor/", fornecedor_views.FornecedorGetView.as_view(), name="fornecedores"),
    path("fornecedor/<int:id>/",fornecedor_views.FornecedorGetByIdView.as_view(),name="fornecedor_detail",),
    path("fornecedor/create/",fornecedor_views.FornecedorPostView.as_view(),name="fornecedor_create"),
    path("fornecedor/update/<int:id>/",fornecedor_views.FornecedorPutView.as_view(),name="fornecedor_update"),
    path("fornecedor/delete/<int:id>/",fornecedor_views.FornecedorDeleteView.as_view(),name="fornecedor_delete"),
    path("produto/",produto_views.ProdutoGetView.as_view(),name="produtos"),
    path("produto/<int:id>/", produto_views.ProdutoGetByIdView.as_view(),name="produto_detail",),
    path("produto/create/", produto_views.ProdutoPostView.as_view(),name="produto_create"),
    path("produto/update/<int:id>/", produto_views.ProdutoPutView.as_view(),name="produto_update"),
    path("produto/delete/<int:id>/", produto_views.ProdutoDeleteView.as_view(),name="produto_delete"),
]
