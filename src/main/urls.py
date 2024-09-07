from django.urls import path
from .views import main_view

urlpatterns = [
    path('',view=main_view,name='main')
]
