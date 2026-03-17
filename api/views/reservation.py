from rest_framework.viewsets import ModelViewSet
from api.models import Reservation
from api.serializers import ReservationSerializer

class ReservationViewSet(ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer