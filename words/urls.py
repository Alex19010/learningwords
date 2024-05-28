from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('create_section/', views.create_section, name='create_section'),
    path('section/<int:section_id>/', views.show_words, name='show_words'),
    path('section/<int:section_id>/create_words/', views.create_words, name='create_words'),
    path('section/<int:section_id>/delete_word/<int:word_id>/', views.delete_word, name='delete_word'),
    path('delete_section/<int:section_id>/', views.delete_section, name='delete_section'),
]
