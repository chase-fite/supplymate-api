"""Supply Request Item join table for SupplyMate"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from supplymateapi.models import SupplyRequestItem
from supplymateapi.views.supply_request import SupplyRequestSerializer
from supplymateapi.views.item import ItemSerializer


class SupplyRequestItemSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for SupplyRequestItem
    Arguments:
        serializers
    """
    supply_request = SupplyRequestSerializer()
    item = ItemSerializer()

    class Meta:
        model = SupplyRequestItem
        url = serializers.HyperlinkedIdentityField(
            view_name='supplyrequestitem',
            lookup_field='id'
        )
        fields = ('id', 'supply_request', 'item', 'requested_quantity')

class SupplyRequestItems(ViewSet):
    """Products for Bangazon"""

    def retrieve(self, request, pk=None):
        """Handle GET requests for single supply_request_item
        Returns:
            Response -- JSON serialized supply_request_item instance
        """
        try:
            supply_request_item = SupplyRequestItem.objects.get(pk=pk)
            serializer = SupplyRequestItemSerializer(supply_request_item, context={'request': request})
            return Response(serializer.data)

        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests to supply_request_items resource
        Returns:
            Response -- JSON serialized list of supply_request_items
        """

        # try:

        #     supply_request_item = SupplyRequestItem.objects.filter()
        #     serializer = SupplyRequestItemSerializer(
        #         supply_request_item, many=True, context={'request': request})
        #     return Response(serializer.data)
        
        # except SupplyRequestItem.DoesNotExist as ex:
        #     pass

        sr_id = self.request.query_params.get('sr_id', None)
        try:
            supply_request_items = SupplyRequestItem.objects.filter(supply_request__id=sr_id)
            serializer = SupplyRequestItemSerializer(supply_request_items, many=True, context={'request': request})
            return Response(serializer.data)    
            
        except SupplyRequestItem.DoesNotExist:
            pass

    def create(self, request):
        """Handle POST operations
        Returns:
            Response -- JSON serialized Orders instance
        """
        new_supply_request_item = SupplyRequestItem()
        new_supply_request_item.supply_request_id = request.data['supply_request_id']
        new_supply_request_item.item_id = request.data['item_id']
        new_supply_request_item.requested_quantity = request.data['requested_quantity']
        new_supply_request_item.save()

        serializer = SupplyRequestItemSerializer(new_supply_request_item, context={'request': request})

        return Response(serializer.data)