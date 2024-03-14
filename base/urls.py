from django.urls import path
from .views import TaskList,TaskCreate,TaskDelete,TaskUpdate,TaskDetail,Customlogin,RegistrationPage
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('login/',Customlogin.as_view(),name='login'),
    path('registration/',RegistrationPage.as_view(),name='registration'),
    path('logout',LogoutView.as_view(next_page='login'),name='logout'),
    path('',TaskList.as_view(),name='tasks'),
    path('task-create',TaskCreate.as_view(),name='new-task'),
    path('task-delete/<int:pk>',TaskDelete.as_view(),name='delete-task'),
    path('task-update/<int:pk>',TaskUpdate.as_view(),name='update-task'),
    path('task-detail',TaskDetail.as_view(),name='detail'),
    
]
