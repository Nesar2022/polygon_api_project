from rest_framework import viewsets
from .models import PolygonRegion
from .serializers import PolygonRegionSerializer

class PolygonRegionViewSet(viewsets.ModelViewSet):
    queryset = PolygonRegion.objects.all()
    serializer_class = PolygonRegionSerializer
