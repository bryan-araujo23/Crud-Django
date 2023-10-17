from django.shortcuts import get_object_or_404, render, redirect
from .forms import CarroForm
from .models import Carro


def cadastrar_carro(request):
    form = CarroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('carro_list')
    return render(request, 'carro_form.html', {'form': form})



def listar_carro(request):
    query = request.GET.get("busca")
    if query:
        carro = Carro.objects.filter(modelo__icontains=query)
    else:
        carro = Carro.objects.all()
    return render(request, 'carro_list.html', {'lista': carro})


def editar_carro(request, pk):
    carro = get_object_or_404(Carro, pk=pk)             
    if request.method == 'POST':                        
        form = CarroForm(request.POST, instance=carro)  
        if form.is_valid():
            form.save()
            return redirect('carro_list')
    else:
        form = CarroForm(instance=carro)
    return render(request, 'carro_form.html', {'form': form})

def remover_carro(request, pk):
    carro = Carro.objects.get(pk=pk)
    if request.method == 'POST':
        carro.delete()
        return redirect('carro_list')
    return render(request, 'carro_delete.html', {'carro': carro})