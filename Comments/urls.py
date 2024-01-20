from django.urls import path
from .views import CommentListAPIView, CommentDetailAPIView

urlpatterns = [
    path('comments/', CommentListAPIView.as_view(), name='comment-list'),
    path('comments/<int:pk>/', CommentDetailAPIView.as_view(), name='comment-detail'),
]