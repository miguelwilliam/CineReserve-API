from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import AllowAny
from api.models import Movie
from api.serializers import MovieSerializer

class MovieViewSet(ReadOnlyModelViewSet):
    permission_classes = [AllowAny]
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer