from django.shortcuts import render, redirect
from .forms import CarroForm



def cadastrar_carro(request):
    form = CarroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('carro_list')
    return render(request, 'carro_form.html', {'form': form})
