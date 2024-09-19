from django import forms

from todo_app.models import Todo1


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo1
        fields = "__all__"