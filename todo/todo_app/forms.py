from tkinter import Widget
from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = "__all__"


    def __init__(self, *args, **kwargs):
        super(TodoForm, self).__init__(*args, **kwargs)
        self.fields['todo'].label = ''
        self.fields['todo'].widget.attrs.update(placeholder = 'add todo')
        self.fields['todo'].widget.attrs.update({'class' : 'input'})
        