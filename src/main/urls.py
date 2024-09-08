from django.urls import path
from .views import main_view, home_view

urlpatterns = [
    path('',view=main_view,name='main'),
    path('home/',view=home_view,name='home')
]
