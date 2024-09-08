from django.urls import path
from .views import log_view, RegisterView

urlpatterns = [
    path('login/',log_view ,name='login'),
  path('register/', RegisterView.as_view(), name='register'),
]
