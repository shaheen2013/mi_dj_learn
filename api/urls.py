from django.urls import path
from api.views import posts

urlpatterns = [
  path('posts', posts, name='posts'),
  path('posts/<int:pk>', posts, name='post'),
]