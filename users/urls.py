from django.urls import path
import users.views as views

urlpatterns = [
    path('register/', views.register, name='register'),
]