from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import AllowAny
from api.models import Session
from api.serializers import SessionSerializer

class SessionViewSet(ReadOnlyModelViewSet):
    permission_classes = [AllowAny]
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

    def get_queryset(self):
        queryset = Session.objects.all().select_related('movie', 'room')
        movie_id = self.request.query_params.get('movie')

        if movie_id and movie_id.isdigit():
            queryset = queryset.filter(movie_id=movie_id)

        return queryset