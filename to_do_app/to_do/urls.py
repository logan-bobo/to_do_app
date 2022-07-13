from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import (
    TaskList,
    TaskCreate,
    TaskUpdate,
    TaskDelete,
    UserLogin,
    Register,
)

urlpatterns = [
    # Homepage
    path('', TaskList.as_view(), name='tasks'),

    # Task operations
    path('create-task/', TaskCreate.as_view(), name='create-task'),
    path('update-task/<int:pk>/', TaskUpdate.as_view(), name='update-task'),
    path('delete-task/<int:pk>/', TaskDelete.as_view(), name='delete-task'),

    # User Authentication Views
    path('login/', UserLogin.as_view(), name='user-login'),
    path('logout/', LogoutView.as_view(next_page='user-login'), name='user-logout'),
    path('register/', Register.as_view(), name='user-register'),
]

