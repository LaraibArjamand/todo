from django.urls import path

from .views import create_list, create_task, delete_list, delete_task, detail_list, mark_task

urlpatterns = [
    path("create/lists", create_list, name="create_list"),
    path("create/task", create_task, name="create_task"),
    path("delete/task/<int:id>", delete_task, name="delete_task"),
    path("mark/task/<int:id>", mark_task, name="mark_task"),
    path("detail/lists/<int:id>", detail_list, name="detail_list"),
    path("delete/lists/<int:id>", delete_list, name="delete_list"),
]
