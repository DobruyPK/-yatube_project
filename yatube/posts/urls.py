from django.urls import path
from . import views
app_name = 'posts'

urlpatterns = [
    # Главная страница
    path('', views.index),
    path('group/<slug:slug>/', views.group_posts, name='posts_list'),
    path('yatube/', views.index, name='logo')
]
