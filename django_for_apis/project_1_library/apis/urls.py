from django.urls import path
from apis.views import BookAPIView

urlpatterns = [
    path("", BookAPIView.as_view()),
]
