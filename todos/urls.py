from django.urls import path
from todos import views

urlpatterns = [
    path('', views.TodoListView.as_view(), name='todo_list_view'),
    path('todo/', views.TodoListCreateView.as_view(),
         name='todo_list_create_view'),
    path('todo/<int:todo_list_id>', views.TodoListEditView.as_view(),
         name='todo_list_update_view'),
]
