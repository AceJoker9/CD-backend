from django.urls import path
from . import views

urlpatterns = [
    path('', views.tracks_list),
    path('tracks/<int:pk>/', views.track_detail, name='track_detail'),
    path('tracks/create/', views.create_song, name='create_song'),
    path('tracks/update/<int:pk>/', views.update_song, name='update_song'),
    path('tracks/delete/<int:pk>/', views.delete_song, name='delete_song'),
]

