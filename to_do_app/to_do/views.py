from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Task


class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')
    template_name = 'to_do/create_task.html'


class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')
    template_name = 'to_do/create_task.html'


class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'to_do/all_tasks.html'


class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'to_do/single_task.html'

