from rest_framework.serializers import ModelSerializer
from Reserva.models import Reserva


class AgendamentoModelSerializer(ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'
