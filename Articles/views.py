from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework import status
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

    #odstránenie článku
    def remove_article(self, request, pk=None):
        try:
            article = self.get_object()
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Article.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    #získanie detailu článku s možnosťou zahrnutia specification
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


        #úprava článku
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)