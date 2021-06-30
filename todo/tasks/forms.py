from django.forms.forms import Form
from todo import tasks
from django import forms
from django import forms
from django.forms import ModelForm

from .models import *


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = '__all__'