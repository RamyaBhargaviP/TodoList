from django.urls import path,include
from . import views

urlpatterns = [
                path('todo/',views.todoview,name='todo'),
                path('todoadd/',views.todoadd,name="add"),
                ]