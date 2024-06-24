from django.shortcuts import render, get_object_or_404
from .models import Categoria, Projeto


def home(request):
    categorias = Categoria.objects.all()
    portfolio = Projeto.objects.all()

    return render(
        request,
        'home.html',
        {
            'categorias': categorias,
            'portfolio': portfolio
        }
    )


def portfolio(request):
    categorias = Categoria.objects.all()
    projetos = Projeto.objects.all()

    return render(
        request,
        'portfolio.html',
        {
            'categorias': categorias,
            'projetos': projetos
        }
    )


def categoria(request, categoria_id):
    categorias = Categoria.objects.all()

    categoria = get_object_or_404(Categoria, id=categoria_id)
    projetos = Projeto.objects.filter(categoria=categoria)

    return render(
        request,
        'portfolio.html',
        {
            'categorias': categorias,
            'projetos': projetos,
            'categoria': categoria
        }
    )


def search(request):
    query = request.GET.get('q')
    if query:
        results = Projeto.objects.filter(titulo__icontains=query)
    else:
        results = Projeto.objects.none()
    return render(request, 'pesquisa.html', {'results': results})
