from rest_framework import viewsets
from region.api import serializers
from region import models

class RegionsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RegionSerializers
    queryset = models.Regions.objects.all()
