from django.urls import path
from .views import cadastrar_carro, listar_carro, editar_carro


urlpatterns = [
    path('cadastrar_carro/', cadastrar_carro, name='cadastrar_carro'),
    path('listar_carro/', listar_carro, name='carro_list'),
    path('editar_carro/<int:pk>', editar_carro, name='editar_carro'),
]