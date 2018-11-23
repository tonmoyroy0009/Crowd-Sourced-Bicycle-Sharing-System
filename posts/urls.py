from django.urls import path, include
from . import views

urlpatterns = [
    path('post', views.post, name='post'),
    path('<int:post_id>', views.detail, name='detail'),
]