from django.urls import include, path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('create/', views.create_post, name='create_post'),
]
