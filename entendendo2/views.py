from django.shortcuts import render
from django.http import HttpResponse
from .models import entendendo2
from django.views.generic import ListView, CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.

class TodoListView(ListView):
    model = entendendo2


class TodoCreateView(CreateView):
    model = entendendo2
    fields = ["title", "deadline"]
    success_url = reverse_lazy("entendendo2_list")

class TodoUpdateView(UpdateView):
    model = entendendo2
    fields = ["title", "deadline"]
    success_url = reverse_lazy("entendendo2_list")

class TodoDeleteView(DeleteView):
    model = entendendo2
    success_url = reverse_lazy("entendendo2_list")