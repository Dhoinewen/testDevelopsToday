from django.urls import path, include

from .views import CommentsAPIView, PostViewSet
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'post', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('list', PostAPIList.as_view()),
    # path('list/<int:pk>/', PostAPIUpdate.as_view()),
    # path('list/post/<int:pk>/', PostAPIDetailView.as_view()),
    path('comments', CommentsAPIView.as_view()),
    path('comments/<int:pk>/', CommentsAPIView.as_view()),
]