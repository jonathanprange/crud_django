from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from region import serializers
from region import models
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

class RegionsViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    
    serializer_class = serializers.RegionSerializers
    queryset = models.Regions.objects.all()

    @method_decorator(cache_page(60))
    def dispatch(self, *args, **kwargs):
        return super(RegionsViewSet, self).dispatch(*args, **kwargs)