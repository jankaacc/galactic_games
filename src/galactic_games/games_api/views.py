from rest_framework.generics import ListAPIView
from rest_framework.response import Response


from gladiators.serializers import GladiatorSerializer
from gladiators.models import Gladiator



class GladiatorListView(ListAPIView):
    """Test API ViewSet."""
    queryset = Gladiator.objects.all()
    serializer_class = GladiatorSerializer