from django.urls import path
from .views import *

urlpatterns = [
    path("movies", movie_list),
    path("movies/<int:pk>", movie_detail),
    path("movies/<int:pk>/reviews", review_list),
    path("actors", actor_list),
    path("actors/<int:pk>", actor_detail),
]
