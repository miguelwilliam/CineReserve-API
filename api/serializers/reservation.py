from rest_framework import serializers
from api.models import Reservation

class ReserveSeatsSerializer(serializers.Serializer):
    seats = serializers.ListField(
        child=serializers.IntegerField(),
        allow_empty=False
    )

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'