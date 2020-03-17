"""Products for Bangazon"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
import sqlite3
from supplymateapi.models import Item


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for Items
    Arguments:
        serializers
    """
    class Meta:
        model = Item
        url = serializers.HyperlinkedIdentityField(
            view_name='item',
            lookup_field='id'
        )
        fields = ('id', 'url', 'name', 'description', 'serial_number', 'stock', 'quantity', 'item_type_id', 'address_id', 'storage_location', 'price')
        depth = 2

class Items(ViewSet):
    """Items for SupplyMate"""

    def retrieve(self, request, pk=None):
        """Handle GET requests for single Item
        Returns:
            Response -- JSON serialized Item instance
        """
        try:
            item = Item.objects.get(pk=pk)
            serializer = ItemSerializer(item, context={'request': request})
            return Response(serializer.data)

        except Exception as ex:
            return HttpResponseServerError(ex)

    # was a little unsure of what to put in the except block here
    def list(self, request):
        """Handle GET requests to Items resource
        Returns:
            Response -- JSON serialized list of Items
        """
        try:
            items = Item.objects.all()
            serializer = ItemSerializer(items, many=True, context={'request': request})
            return Response(serializer.data)    
            
        except Item.DoesNotExist:
            pass

    def create(self, request):
        """Handle POST operations
        Returns:
            Response -- JSON serialized Items instance
        """
        new_item = Item()
        new_item.name = request.data["name"]
        new_item.description = request.data["description"]
        new_item.serial_number = request.data["serial_number"]
        new_item.stock = request.data["stock"]
        new_item.quantity = request.data["quantity"]
        new_item.item_type_id = request.data["item_type_id"]
        new_item.address_id = request.data["address_id"]
        new_item.storage_location = request.data["storage_location"]
        new_item.price = request.data["price"]
        new_item.save()

        serializer = ItemSerializer(new_item, context={'request': request})

        return Response(serializer.data)

    def update(self, request, pk=None):
        """Handle PUT requests for a item
        Returns:
            Response -- Empty body with 204 status code
        """
        item = Item.objects.get(pk=pk)
        item.name = request.data["name"]
        item.description = request.data["description"]
        item.serial_number = request.data["serial_number"]
        item.stock = request.data["stock"]
        item.quantity = request.data["quantity"]
        item.item_type_id = request.data["item_type_id"]
        item.address_id = request.data["address_id"]
        item.storage_location = request.data["storage_location"]
        item.price = request.data["price"]
        item.save()

        serializer = ItemSerializer(item, context={'request': request})

        return Response(serializer.data)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single item
        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            item = Item.objects.get(pk=pk)
            item.delete()
            
            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Item.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
