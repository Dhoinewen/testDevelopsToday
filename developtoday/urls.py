from django.urls import path

from .views import CommentsAPIView, PostAPIList, PostAPIUpdate, PostAPIDetailView

urlpatterns = [
    path('list', PostAPIList.as_view()),
    path('list/<int:pk>/', PostAPIUpdate.as_view()),
    path('list/post/<int:pk>/', PostAPIDetailView.as_view()),
    path('comments', CommentsAPIView.as_view()),
    path('comments/<int:pk>/', CommentsAPIView.as_view()),
]