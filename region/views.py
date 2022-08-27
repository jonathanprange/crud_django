from os import stat
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Regions
from .api.serializers import RegionSerializers
import coreapi
from rest_framework.schemas import AutoSchema

class RegionsViewSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() in ['post', 'put']:
            extra_fields = [
                coreapi.Field('name')
            ]
        manual_fields = super().get_manual_fields(path, method)

        return manual_fields + extra_fields

class RegionsCollection(APIView):
    schema = RegionsViewSchema()

    def get(self, request):
        items = Regions.objects.all()
        serializer = RegionSerializers(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RegionSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegionsDetail(APIView):
    schema = RegionsViewSchema()

    def delete(self, request, pk):
        item = Regions.objects.get(id=pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        item = Regions.objects.get(id=pk)
        serializer = RegionSerializers(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
