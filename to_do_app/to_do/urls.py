from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import (
    TaskList,
    TaskDetail,
    TaskCreate,
    TaskUpdate,
    TaskDelete,
    UserLogin
)

urlpatterns = [
    # Homepage
    path('', TaskList.as_view(), name='tasks'),

    # Task operations
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('create-task/', TaskCreate.as_view(), name='create-task'),
    path('update-task/<int:pk>/', TaskUpdate.as_view(), name='update-task'),
    path('delete-task/<int:pk>/', TaskDelete.as_view(), name='delete-task'),

    # User Authentication Views
    path('login/', UserLogin.as_view(), name='user-login'),
    path('logout/', LogoutView.as_view(next_page='user-login'), name='user-logout')
]

