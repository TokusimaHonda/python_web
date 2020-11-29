from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from .models import TodoModel
from django.urls import reverse_lazy


# Create your views here.

class ToDoList(ListView):
    template_name = 'list.html'
    model =  TodoModel

class ToDoDetail(DetailView):
    template_name = 'detail.html'
    model = TodoModel

class ToDoCreate(CreateView):
    template_name = 'create.html'
    model = TodoModel
    fields = ('title','memo','priority','duedate')
    success_url = reverse_lazy('list')

class ToDoDelete(DeleteView):
    template_name = 'delete.html'
    model = TodoModel
    success_url = reverse_lazy('list')

class ToDoUpdate(UpdateView):
    template_name = 'update.html'
    model = TodoModel
    fields = ('title','memo','priority','duedate')
    success_url = reverse_lazy('list')
