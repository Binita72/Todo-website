from django.urls import path
from . import views


urlpatterns =[
    path('',views.index,name='home'),
    path('create/',views.create_todo,name='create-todo'),
    path('todo/<int:id>/',views.todo_detail,name='todo'),
    path('todo-delete/<int:id>/',views.todo_delete,name='todo-delete'),
    path('edit-todo/<int:id>/',views.todo_edit,name='todo-edit'),
]