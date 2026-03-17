from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from api.models import Session
from api.serializers import SessionSerializer

class SessionViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Session.objects.all()
    serializer_class = SessionSerializer