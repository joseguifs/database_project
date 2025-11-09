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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('categoria/', views.CategoriaGetView.as_view(), name = 'categorias'),
    path('categoria/<int:id>/', views.CategoriaGetByIdView.as_view(), name = 'categoria_detail'),
    path('categoria/create/', views.CategoriaPostView.as_view(), name = 'categoria_create'),
    path('categoria/update/<int:id>/', views.CategoriaPutView.as_view(), name = 'categoria_update'),
    path('categoria/delete/<int:id>/', views.CategoriaDeleteView.as_view(), name = 'categoria_delete'),
    
]
