from django.shortcuts import render
from django.http import HttpResponse
from .models import entendendo2
# Create your views here.


def home(request):
    return render(request, "entendendo2/home.html")

def home(request):
    return render(request, "entendendo2/entendendo2_list.html")

def entendendo2_list(request):
    nome = 'Rodrigo'  # Indentado corretamente
    alunos = ['1. Ana', '2. José', '3. Bia']  # Indentado corretamente
    return render(request, "entendendo2/entendendo2_list.html", {"nome": nome, "lista_alunos": alunos})  # Corrigida a indentação

# Primeira função
def entendendo2_list_old(request):
    nome = 'Rodrigo'
    alunos = ['1. Ana', '2. José', '3. Bia']
    return render(request, "entendendo2/entendendo2_list.html", {"nome": nome, "lista_alunos": alunos})

# Segunda função
def entendendo2_list(request):
    entendendo2_list = entendendo2.objects.all()
    return render(request, "entendendo2/entendendo2_list.html", {"entendendendo2": entendendo2_list})
