from django.urls import path
from .views import cadastrar_carro


urlpatterns = [
    path('cadastrar_carro/', cadastrar_carro, name='cadastrar_carro'),
]