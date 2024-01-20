from rest_framework import generics
from .models import Comment
from .serializers import CommentSerializer

class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    # def get_queryset(self):
    #     queryset = Comment.objects.all()
    #     post = self.request.query_params.get('post')
    #     if post is not None:
    #         queryset = queryset.filter(post__exact=post)
    #
    #         return queryset