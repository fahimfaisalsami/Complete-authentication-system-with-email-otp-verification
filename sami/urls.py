from django.urls import path
from .views import hello, all_prof, delete_prof, update_prof, download_info, TaskView, delete_task, update_task

urlpatterns = [
    path('hello/', hello, name='hello'),
    path('all_prof/', all_prof, name='all_prof'),
    path('delete_prof/<int:id>', delete_prof, name='delete_prof'),
    path('update_prof/<int:id>', update_prof, name='update_prof'),
    path('download_info/<int:id>/', download_info, name='download_info'),
    path('tasks/', TaskView.as_view(), name='tasks'),
    path('delete_task/<int:id>/', delete_task, name='delete_task'),
    path('update_task/<int:id>/', update_task, name='update_task'),
]