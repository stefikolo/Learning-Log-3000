from django.urls import path
import users.views as views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
]