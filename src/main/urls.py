from django.urls import path
from .views import main_view, home_view, list_view, listing_view, edit_view, like_listing_view

urlpatterns = [
    path('',view=main_view,name='main'),
    path('home/',view=home_view,name='home'),
    path('list/',view=list_view,name='list'),
    path('listing/<str:id>',view=listing_view,name='listing'),
    path('listing/<str:id>/edit/',view=edit_view,name='edit'),
    path('listing/<str:id>/like/',view=like_listing_view,name='like_listing')
]
