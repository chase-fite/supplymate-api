"""Roles for SupplyMate"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
import sqlite3
from supplymateapi.models import Role


class RoleSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for Roles
    Arguments:
        serializers
    """
    class Meta:
        model = Role
        url = serializers.HyperlinkedIdentityField(
            view_name='role',
            lookup_field='id'
        )
        fields = ('id', 'url', 'name')

class Roles(ViewSet):
    """Items for SupplyMate"""

    def retrieve(self, request, pk=None):
        """Handle GET requests for single Role
        Returns:
            Response -- JSON serialized Role instance
        """
        try:
            role = Role.objects.get(pk=pk)
            serializer = RoleSerializer(role, context={'request': request})
            return Response(serializer.data)

        except Exception as ex:
            return HttpResponseServerError(ex)

    # was a little unsure of what to put in the except block here
    def list(self, request):
        """Handle GET requests to Roles resource
        Returns:
            Response -- JSON serialized list of Roles
        """
        try:
            roles = Role.objects.all()
            serializer = RoleSerializer(roles, many=True, context={'request': request})
            return Response(serializer.data)    
            
        except Role.DoesNotExist:
            pass