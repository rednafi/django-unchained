from django.urls import path, include
from . import views

urlpatterns = [path("<book_id>/", views.dummy_catalog)]
