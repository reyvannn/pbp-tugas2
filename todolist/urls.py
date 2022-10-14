from django.urls import path
from todolist.views import show_homepage, login_user, logout_user, create_task, register, get_json, add_task_json

app_name = 'todolist'

urlpatterns = [
    path('', show_homepage, name='show_homepage'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create_task'),
    path('json/', get_json, name='get_json'),
    path('add/', add_task_json, name='add_task_json'),
]