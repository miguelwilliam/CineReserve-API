from rest_framework.viewsets import ModelViewSet
from api.models import Session
from api.serializers import SessionSerializer

class SessionViewSet(ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer