"""ItemTypes for SupplyMate"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
import sqlite3
from supplymateapi.models import ItemType


class ItemTypeSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for Item Types
    Arguments:
        serializers
    """
    class Meta:
        model = ItemType
        url = serializers.HyperlinkedIdentityField(
            view_name='itemtype',
            lookup_field='id'
        )
        fields = ('id', 'url', 'name')

class ItemTypes(ViewSet):
    """Items for SupplyMate"""

    def retrieve(self, request, pk=None):
        """Handle GET requests for single Item Type
        Returns:
            Response -- JSON serialized Item Type instance
        """
        try:
            item_type = ItemType.objects.get(pk=pk)
            serializer = ItemTypeSerializer(item_type, context={'request': request})
            return Response(serializer.data)

        except Exception as ex:
            return HttpResponseServerError(ex)

    # was a little unsure of what to put in the except block here
    def list(self, request):
        """Handle GET requests to Items resource
        Returns:
            Response -- JSON serialized list of Item Types
        """
        try:
            item_types = ItemType.objects.all()
            serializer = ItemTypeSerializer(item_types, many=True, context={'request': request})
            return Response(serializer.data)    
            
        except ItemType.DoesNotExist:
            pass

    def create(self, request):
        """Handle POST operations
        Returns:
            Response -- JSON serialized Items instance
        """
        new_item_type = ItemType()
        new_item_type.name = request.data["name"]
        new_item_type.save()

        serializer = ItemTypeSerializer(new_item_type, context={'request': request})

        return Response(serializer.data)

    def update(self, request, pk=None):
        """Handle PUT requests for a item
        Returns:
            Response -- Empty body with 204 status code
        """
        item_type = ItemType.objects.get(pk=pk)
        item_type.name = request.data["name"]
        item_type.save()

        serializer = ItemTypeSerializer(item_type, context={'request': request})

        return Response(serializer.data)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single item
        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            item_type = ItemType.objects.get(pk=pk)
            item_type.delete()
            
            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except ItemType.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)