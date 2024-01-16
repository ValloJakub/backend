from rest_framework import routers
from .views import ArticleViewSet
from django.urls import path

router = routers.DefaultRouter()
router.register(r'articles', ArticleViewSet)

urlpatterns = router.urls

# Endpoint pre odstránenie článku
urlpatterns += [
    path('articles/<int:pk>/remove/', ArticleViewSet.as_view({'post': 'remove_article'}), name='remove-article'),
]