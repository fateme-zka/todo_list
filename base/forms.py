from django.forms import ModelForm, forms
from .models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'completed')
