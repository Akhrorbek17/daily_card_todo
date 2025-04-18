from django.urls import path
from . import views

app_name = 'card'

urlpatterns = [
    path('', views.AdminDashboardView.as_view() , name = 'dashboard'),
    # path("task/", views.task_board, name="task_board" ),
    path('add/', views.add_task, name="add_task"),
    path("update/<int:task_id>/<str:status>/" , views.update_status, name = 'update_task'),
    path('delete/<int:task_id>/', views.delete_task, name="delete_task"),
]