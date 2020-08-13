from django.urls import path

# Create your views here.
from . import views

urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name="signup"),
]
