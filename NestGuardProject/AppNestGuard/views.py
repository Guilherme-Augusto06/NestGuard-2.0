from .models import *
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import OrcamentoForm

# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')




def orcamento(request):
    """
    Exibe e processa o formulário de orçamento.
    """
    if request.method == 'POST':
        form = OrcamentoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Orçamento registrado com sucesso!')
            return redirect('orcamento')  # Redireciona para a mesma página após o sucesso
        else:
            messages.error(request, 'Houve um erro no registro. Verifique os dados e tente novamente.')
    else:
        form = OrcamentoForm()

    # Renderiza o formulário na página de orçamento
    return render(request, 'orcamento.html', {'form': form})



def registro_orcamento(request):
    """
    View para exibir e processar o formulário de registro de orçamento.
    """
    if request.method == 'POST':
        form = OrcamentoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Orçamento registrado com sucesso!')
            return redirect('pagina_de_sucesso')  # Substitua pela URL da página de sucesso
        else:
            messages.error(request, 'Houve um erro no registro. Verifique os dados e tente novamente.')
    else:
        form = OrcamentoForm()

    # Adicione debug temporário
    print(f"Formulário: {form}")

    return render(request, 'registro_orcamento.html', {'form': form})

