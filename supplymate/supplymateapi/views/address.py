"""Addresses for SupplyMate"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
import sqlite3
from supplymateapi.models import Address


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for Address
    Arguments:
        serializers
    """
    class Meta:
        model = Address
        url = serializers.HyperlinkedIdentityField(
            view_name='address',
            lookup_field='id'
        )
        fields = ('id', 'street', 'city', 'state', 'zip_code')

class Addresses(ViewSet):
    """Addresses for SupplyMate"""

    def retrieve(self, request, pk=None):
        """Handle GET requests for single Address
        Returns:
            Response -- JSON serialized Address instance
        """
        try:
            address = Address.objects.get(pk=pk)
            serializer = AddressSerializer(address, context={'request': request})
            return Response(serializer.data)

        except Exception as ex:
            return HttpResponseServerError(ex)

    # was a little unsure of what to put in the except block here
    def list(self, request):
        """Handle GET requests to Addresses resource
        Returns:
            Response -- JSON serialized list of Addresses
        """
        try:
            addresses = Address.objects.all()
            serializer = AddressSerializer(addresses, many=True, context={'request': request})
            return Response(serializer.data)    
            
        except Address.DoesNotExist:
            pass

    def create(self, request):
        """Handle POST operations
        Returns:
            Response -- JSON serialized Addresses instance
        """
        new_address = Address()
        new_address.street = request.data["street"]
        new_address.city = request.data["city"]
        new_address.state = request.data["state"]
        new_address.zip_code = request.data["zip_code"]
        new_address.save()

        serializer = AddressSerializer(new_address, context={'request': request})

        return Response(serializer.data)

    def update(self, request, pk=None):
        """Handle PUT requests for an address
        Returns:
            Response -- Empty body with 204 status code
        """
        address = Address.objects.get(pk=pk)
        address.street = request.data["street"]
        address.city = request.data["city"]
        address.state = request.data["state"]
        address.zip_code = request.data["zip_code"]
        address.save()

        serializer = AddressSerializer(address, context={'request': request})

        return Response(serializer.data)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single address
        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            address = Address.objects.get(pk=pk)
            address.delete()
            
            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Address.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)