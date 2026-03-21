from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db import transaction
from django.utils import timezone
from api.models import Reservation, SessionSeat
from api.serializers import ReservationSerializer, ReserveSeatsSerializer


class ReservationViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def get_queryset(self):
        user = self.request.user

        possibly_expired_seats = (
            SessionSeat.objects
            .filter(
                status=SessionSeat.SeatStatus.RESERVED
            )
        )

        for seat in possibly_expired_seats:
            seat.release_if_expired()

        print('Bancos expirados:',len(possibly_expired_seats))

        return Reservation.objects.filter(user=user)
    
    def get_serializer_class(self):
        if self.action == "reserve":
            return ReserveSeatsSerializer
        return super().get_serializer_class()
 
    @action(detail=False, methods=['post']) # DETAIL = FALSE -> AÇÕES EM LISTAS
    def reserve(self, request):
        serializer = ReserveSeatsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        seat_ids = serializer.validated_data["seats"]

        with transaction.atomic():
            seats = SessionSeat.objects.select_for_update().filter(id__in=seat_ids)

            if seats.count() != len(seat_ids):
                return Response({"error": "Invalid seats"}, status=400)

            for seat in seats:
                seat.release_if_expired()

                if seat.status != SessionSeat.SeatStatus.AVAILABLE:
                    return Response({"error": "Seat not available"}, status=400)

            reservation = Reservation.objects.create(user=request.user)

            for seat in seats:
                seat.status = SessionSeat.SeatStatus.RESERVED
                seat.reserved_at = timezone.now()
                seat.reservation = reservation
                seat.save()

        return Response({"reservation_id": reservation.id})

    @action(detail=True, methods=['post']) # DETAIL = TRUE -> AÇÕES INDIVIDUAIS
    def checkout(self, request, pk=None):
        reservation = self.get_object()

        if reservation.status != Reservation.ReservationStatus.PENDING:
            return Response({"error": "Invalid checkout, either not reserved or already expired!"}, status=400)
        if request.user.id != reservation.user.id:
            return Response({"error": "Invalid checkout, the reservation belongs to other user!"}, status=400)


        with transaction.atomic():
            seats = reservation.sessionseat_set.select_for_update()

            for seat in seats:
                if seat.is_expired():
                    reservation.status = Reservation.ReservationStatus.CANCELLED
                    reservation.save()
                    return Response({"error": "Reservation expired"}, status=400)

                seat.status = SessionSeat.SeatStatus.PURCHASED
                seat.save()

            reservation.status = Reservation.ReservationStatus.CONFIRMED
            reservation.save()

        return Response({"message": "Purchase completed"})

    @action(detail=False, methods=['get']) # DETAIL = FALSE -> AÇÕES EM LISTAS
    def my_tickets(self, request):
        reservations = Reservation.objects.filter(
            user=request.user,
            sessionseat__status=SessionSeat.SeatStatus.PURCHASED,
            sessionseat__session__start_time__gte=timezone.now()
        ).distinct()

        serializer = self.get_serializer(reservations, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get']) # DETAIL = FALSE -> AÇÕES EM LISTAS
    def history(self, request):
        reservations = Reservation.objects.filter(
            user=request.user,
            sessionseat__status="purchased"
        ).distinct()

        serializer = self.get_serializer(reservations, many=True)
        return Response(serializer.data)