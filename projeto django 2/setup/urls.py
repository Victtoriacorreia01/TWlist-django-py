from django.contrib import admin
from django.urls import path

from todos.views import TodosListView, TodosCreateView, TodosUpdateView, TodosDeleteView, TodosCompleteView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TodosListView.as_view(), name="todos_list"),
    path("create", TodosCreateView.as_view(), name="todos_create"),
    path("update/<int:pk>", TodosUpdateView.as_view(), name="todos_update"),
    path("delete/<int:pk>", TodosDeleteView.as_view(), name="todos_delete"),
    path("complete/<int:pk>", TodosCompleteView.as_view(), name="todos_complete"),


 
]
