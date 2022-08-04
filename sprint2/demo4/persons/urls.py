from django.urls import path

# from .views import PersonDetailView, PersonView
from . import views

urlpatterns = [
    path("persons/", views.PersonView.as_view()),
    path("persons/<int:person_id>/", views.PersonDetailView.as_view()),
    path("persons/search/", views.PersonSearchView.as_view()),
]
