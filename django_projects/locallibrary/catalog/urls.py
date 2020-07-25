from django.urls import include, path

from . import views

urlpatterns = [path("<book_id>/", views.dummy_catalog)]
