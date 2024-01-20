from rest_framework import viewsets
from .models import Article
from .serializers import ArticleSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    # Filter - vráti len články NHL
    def get_queryset(self):
        queryset = Article.objects.all()
        specification = self.request.query_params.get('specification')
        if specification is not None:
            queryset = queryset.filter(specification=specification)
        return queryset