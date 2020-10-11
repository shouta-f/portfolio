from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import WilldoModel
from django.urls import reverse_lazy

# Create your views here.
class WilldoList(ListView):
    template_name = 'list.html'
    model = WilldoModel

class WilldoDetail(DetailView):
    template_name = 'detail.html'
    model = WilldoModel

class WilldoCreate(CreateView):
    template_name = 'create.html'
    model = WilldoModel
    fields = ('title', 'note', 'task_type', 'priority', 'date')
    success_url = reverse_lazy('list')

class WilldoDelete(DeleteView):
    template_name = 'delete.html'
    model = WilldoModel
    success_url = reverse_lazy('list')

class WilldoUpdate(UpdateView):
    template_name = 'update.html'
    model = WilldoModel
    fields = ('title', 'note', 'task_type', 'priority', 'date')
    success_url = reverse_lazy('list')
