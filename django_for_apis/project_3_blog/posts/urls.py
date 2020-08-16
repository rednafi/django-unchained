from django.urls import path

#from posts.views import PostList, PostDetail, UserList, UserDetail

# traditional django View class based urls

# urlpatterns = [
#     path("users/", UserList.as_view(), name="user_list"),
#     path("users/<int:pk>/", UserDetail.as_view(), name="user_detail"),
#     path("<int:pk>/", PostDetail.as_view(), name="post_detail"),
#     path("", PostList.as_view(), name="post_list"),
# ]

# drf router that uses viewsets

from posts.views import UserViewSet, PostViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register("users", UserViewSet, basename="users")
router.register("", PostViewSet, basename="posts")
urlpatterns = router.urls
