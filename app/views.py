from django.shortcuts import render, redirect
from .forms import CarroForm
from .models import Carro


def cadastrar_carro(request):
    form = CarroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('carro_list')
    return render(request, 'carro_form.html', {'form': form})



def listar_carro(request):
    carros = Carro.objects.all()
    return render(request, 'carro_list.html', {'lista': carros})