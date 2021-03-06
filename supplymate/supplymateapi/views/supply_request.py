"""Supply Requests for SupplyMate"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
import sqlite3
from supplymateapi.models import SupplyRequest
from supplymateapi.views.employee import EmployeeSerializer
from supplymateapi.views.address import AddressSerializer
from supplymateapi.views.status import StatusSerializer
from supplymateapi.views.item import ItemSerializer


class SupplyRequestSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for Supply Requests
    Arguments:
        serializers
    """
    employee = EmployeeSerializer()
    address = AddressSerializer()
    status = StatusSerializer()
    items = ItemSerializer(many=True)

    class Meta:
        model = SupplyRequest
        url = serializers.HyperlinkedIdentityField(
            view_name='supplyrequest',
            lookup_field='id'
        )
        fields = ('id', 'employee', 'address', 'delivery_date_time', 'status', 'items')
        depth = 2

class SupplyRequests(ViewSet):
    """Supply Requests for SupplyMate"""

    def retrieve(self, request, pk=None):
        """Handle GET requests for single Supply Request
        Returns:
            Response -- JSON serialized Supply Request instance
        """
        try:
            supply_request = SupplyRequest.objects.get(pk=pk)
            serializer = SupplyRequestSerializer(supply_request, context={'request': request})
            return Response(serializer.data)

        except Exception as ex:
            return HttpResponseServerError(ex)

    # was a little unsure of what to put in the except block here
    def list(self, request):
        """Handle GET requests to Supply Requests resource
        Returns:
            Response -- JSON serialized list of Supply Requests
        """
        status = self.request.query_params.get('status', None)
        if(status == 'pending'):
            try:
                role = request.auth.user.employee.role.name
                if(role == "Remote"):
                    supply_requests = SupplyRequest.objects.filter(status__name='Pending', employee__id=request.auth.user.employee.id).order_by('-delivery_date_time')
                    serializer = SupplyRequestSerializer(supply_requests, many=True, context={'request': request})
                    return Response(serializer.data)    
                else: 
                    supply_requests = SupplyRequest.objects.filter(status__name='Pending').order_by('-delivery_date_time')
                    serializer = SupplyRequestSerializer(supply_requests, many=True, context={'request': request})
                    return Response(serializer.data)

            except SupplyRequest.DoesNotExist:
                pass

        elif(status == 'approved'):
            try:
                role = request.auth.user.employee.role.name
                if(role == "Remote"):
                    supply_requests = SupplyRequest.objects.filter(status__name='Approved', employee__id=request.auth.user.employee.id).order_by('-delivery_date_time')
                    serializer = SupplyRequestSerializer(supply_requests, many=True, context={'request': request})
                    return Response(serializer.data)    
                else: 
                    supply_requests = SupplyRequest.objects.filter(status__name='Approved').order_by('-delivery_date_time')
                    serializer = SupplyRequestSerializer(supply_requests, many=True, context={'request': request})
                    return Response(serializer.data)

            except SupplyRequest.DoesNotExist:
                pass
        
        elif(status == 'complete'):
            try:
                role = request.auth.user.employee.role.name
                if(role == "Remote"):
                    supply_requests = SupplyRequest.objects.filter(status__name='Complete', employee__id=request.auth.user.employee.id).order_by('-delivery_date_time')
                    serializer = SupplyRequestSerializer(supply_requests, many=True, context={'request': request})
                    return Response(serializer.data)    
                else: 
                    supply_requests = SupplyRequest.objects.filter(status__name='Complete').order_by('-delivery_date_time')
                    serializer = SupplyRequestSerializer(supply_requests, many=True, context={'request': request})
                    return Response(serializer.data)

            except SupplyRequest.DoesNotExist:
                pass

    def create(self, request):
        """Handle POST operations
        Returns:
            Response -- JSON serialized Supply Requests instance
        """
        new_supply_request = SupplyRequest()
        new_supply_request.employee_id = request.data["employee_id"]
        new_supply_request.address_id = request.data["address_id"]
        new_supply_request.delivery_date_time = request.data["delivery_date_time"]
        new_supply_request.status_id = request.data["status_id"]
        new_supply_request.save()

        serializer = SupplyRequestSerializer(new_supply_request, context={'request': request})

        return Response(serializer.data)

    def update(self, request, pk=None):
        """Handle PUT requests for a supply request
        Returns:
            Response -- Empty body with 204 status code
        """
        supply_request = SupplyRequest.objects.get(pk=pk)
        supply_request.employee_id = request.data["employee_id"]
        supply_request.address_id = request.data["address_id"]
        supply_request.delivery_date_time = request.data["delivery_date_time"]
        supply_request.status_id = request.data["status_id"]
        supply_request.save()

        serializer = SupplyRequestSerializer(supply_request, context={'request': request})

        return Response(serializer.data)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single supply request
        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            supply_request = SupplyRequest.objects.get(pk=pk)
            supply_request.delete()
            
            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except SupplyRequest.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)