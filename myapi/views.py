from rest_framework import viewsets

from .serializers import MapGETSerializer, MapPOSTSerializer, ValueGETSerializer, ValuePOSTSerializer
from .models import Map, Value


from rest_framework.mixins import (
    CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
)

from rest_framework.viewsets import GenericViewSet


class MapViewSet(viewsets.ModelViewSet):
    queryset = Map.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return MapPOSTSerializer
        return MapGETSerializer



