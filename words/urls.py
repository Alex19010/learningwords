from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('create_section/', views.create_section, name='create_section'),
    path('section/<int:section_id>/', views.show_words, name='show_words'),
    path('section/<int:section_id>/create_words/', views.create_words, name='create_words'),
]
