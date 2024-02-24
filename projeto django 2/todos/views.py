from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect

from .models import Todos


class TodosListView(ListView):
    model = Todos

class TodosCreateView(CreateView):
    model = Todos
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todos_list")

class TodosUpdateView(UpdateView):
    model = Todos
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todos_list")

class TodosDeleteView(DeleteView):
    model = Todos 
    success_url = reverse_lazy("todos_list")

class TodosCompleteView(View):
    def get(self, request, pk):
        todo = get_object_or_404(Todos, pk=pk)
        todo.mark_has_complete()
        return redirect("todos_list")