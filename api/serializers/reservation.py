from rest_framework import serializers
from api.models import Reservation, SessionSeat

class ReserveSeatsSerializer(serializers.Serializer):
    seats = serializers.ListField(
        child=serializers.IntegerField(),
        allow_empty=False
    )

    def validate_seats(self, value):
        seats = SessionSeat.objects.filter(id__in=value)

        if seats.count() != len(value):
            raise serializers.ValidationError("Alguns assentos não existem.")

        # 🔵 pega os session_ids distintos
        session_ids = seats.values_list("session_id", flat=True).distinct()

        if len(session_ids) != 1:
            raise serializers.ValidationError("Os assentos devem ser da mesma sessão.")

        return value

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'