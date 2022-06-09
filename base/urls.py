from django.urls import path
from .views import *

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('task/<str:pk>/', TaskDetail.as_view(), name='task'),
    path('create_task', TaskCreate.as_view(), name='create_task'),
    path('update_task/<str:pk>/', TaskUpdate.as_view(), name='update_task'),

]
