from typing import Any

from django.forms import ModelForm

from todoapp.list.models import List, Task


class ListForm(ModelForm):

    class Meta:
        model = List
        exclude = ["user"]

    def save(self, user=None) -> Any:
        if user is not None:
            self.instance.user = user
        return super().save()


class TaskForm(ModelForm):

    class Meta:
        model = Task
        fields = ["list", "description"]
