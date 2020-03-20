"""Statuses for SupplyMate"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
import sqlite3
from supplymateapi.models import Status


class StatusSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for Roles
    Arguments:
        serializers
    """
    class Meta:
        model = Status
        url = serializers.HyperlinkedIdentityField(
            view_name='status',
            lookup_field='id'
        )
        fields = ('id', 'name')

class Statuses(ViewSet):
    """Statuses for SupplyMate"""

    def retrieve(self, request, pk=None):
        """Handle GET requests for single Status
        Returns:
            Response -- JSON serialized Status instance
        """
        try:
            status = Status.objects.get(pk=pk)
            serializer = StatusSerializer(status, context={'request': request})
            return Response(serializer.data)

        except Exception as ex:
            return HttpResponseServerError(ex)

    # was a little unsure of what to put in the except block here
    def list(self, request):
        """Handle GET requests to Statuses resource
        Returns:
            Response -- JSON serialized list of Statuses
        """
        try:
            statuses = Status.objects.all()
            serializer = StatusSerializer(statuses, many=True, context={'request': request})
            return Response(serializer.data)    
            
        except Status.DoesNotExist:
            pass