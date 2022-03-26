from django.urls import path

from .views import PostAPIView, CommentsAPIView

urlpatterns = [
    path('list', PostAPIView.as_view()),
    path('list/<int:pk>/', PostAPIView.as_view()),
    path('comments', CommentsAPIView.as_view()),
    path('comments/<int:pk>/', CommentsAPIView.as_view()),
]