from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.register_in_view, name='register_in'),
    path('register/', views.register_up_view, name='register_up'),
    path('logout/', views.logout_view, name='logout'),
    ]
