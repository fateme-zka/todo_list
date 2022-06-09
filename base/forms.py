from django.forms import ModelForm, forms
from django import forms

from .models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'completed')


class PositionForm(forms.Form):
    position = forms.CharField()
