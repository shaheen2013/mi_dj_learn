from django.urls import path
from drf.views import TodoView

urlpatterns = [
    path('todos', TodoView.as_view(), name='todos')
]