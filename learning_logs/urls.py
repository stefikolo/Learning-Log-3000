from django.urls import path
import learning_logs.views as views

urlpatterns = [
    path('', views.index, name='index'),

]
