from django.urls import path
from recipes import views as recipe_views

from . import views as user_views

urlpatterns = [
    path("users/", user_views.UserView.as_view()),
    path("users/<int:user_id>/", user_views.UserDetailView.as_view()),
    path("users/<int:user_id>/recipes/", recipe_views.RecipeView.as_view()),
    path(
        "users/<int:user_id>/recipes/<int:recipe_id>/",
        recipe_views.RecipeDetailView.as_view(),
    ),
]
