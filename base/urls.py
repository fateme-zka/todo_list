from django.urls import path
from django.contrib.auth.views import LoginView

from .views import *

urlpatterns = [
    # authentication urls
    path('login/', Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', Register.as_view(), name='register'),

    # CRUD urls
    path('', TaskList.as_view(), name='tasks'),
    path('task/<str:pk>/', TaskDetail.as_view(), name='task'),
    path('create_task', TaskCreate.as_view(), name='create_task'),
    path('update_task/<str:pk>/', TaskUpdate.as_view(), name='update_task'),
    path('delete_task/<str:pk>/', TaskDelete.as_view(), name='delete_task'),

]
