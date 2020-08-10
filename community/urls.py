from django.urls import path
from community import views

urlpatterns = [
    path('', views.daily_commit, name='daily_commit'),
]