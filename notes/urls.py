from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.notes_index ,name='tasks' ),
]