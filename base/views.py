from django.urls import reverse_lazy
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)

from .models import Task
from .forms import TaskForm


class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'  # it was task_list
    queryset = Task.objects.all()


class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'  # it was object


class TaskCreate(CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('tasks')


class TaskUpdate(UpdateView):
    model = Task
    form_class = TaskForm

    def get_success_url(self):
        pk = self.object.pk
        return reverse_lazy('task', kwargs={'pk': pk})
