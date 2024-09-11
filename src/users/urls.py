from django.urls import path
from .views import log_view, logout_view,RegisterView, ProfileView

urlpatterns = [
  path('login/',log_view ,name='login'),
  path('logout/',logout_view ,name='logout'),
  path('register/', RegisterView.as_view(), name='register'),
  path('profile/', ProfileView.as_view(), name='profile'),
]
