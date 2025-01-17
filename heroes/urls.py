from django.urls import path
from . import views

urlpatterns = [
    path('', views.superhero_list, name='hero-list'),
    path('add/', views.add_superhero, name='add-hero'),
    path('<int:pk>/', views.superhero_detail, name='hero-detail'),
    path('<int:pk>/add-image/', views.add_image, name = 'add-image'),
    path('<int:pk>/add-comment/', views.add_comment, name = 'add-comment'),
    path('like/<int:pk>/', views.like_superhero, name = 'like-hero'),
    path('leaderboard/', views.leaderboard_view, name='leaderboard'),
    path('superfan/', views.superfan_view, name='superfan'),
    path('compare/',views.compare_superheroes, name = 'compare-heroes')
]