"""project_3_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from rest_framework.renderers import JSONOpenAPIRenderer

schema_view = get_schema_view(
    title='Blog API',
    url='http://localhost:8000/apis/',
    renderer_classes=[JSONOpenAPIRenderer]
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("apis/v1/", include("posts.urls")),
    path("api-auth/", include("rest_framework.urls")),
    path("apis/v1/rest-auth/", include("rest_auth.urls")),
    path("apis/v1/rest-auth/registration/", include("rest_auth.registration.urls")),
    url("schema/", schema_view),
]
