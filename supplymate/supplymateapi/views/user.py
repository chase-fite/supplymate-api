"""Users for SupplyMate"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
import sqlite3
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for User
    Arguments:
        serializers
    """
    class Meta:
        model = User
        url = serializers.HyperlinkedIdentityField(
            view_name='user',
            lookup_field='id'
        )
        fields = ('id', 'first_name', 'last_name')

class Users(ViewSet):
    """Users for SupplyMate"""

    def retrieve(self, request, pk=None):
        """Handle GET requests for single User
        Returns:
            Response -- JSON serialized User instance
        """
        try:
            user= User.objects.get(pk=pk)
            serializer = UserSerializer(user, context={'request': request})
            return Response(serializer.data)

        except Exception as ex:
            return HttpResponseServerError(ex)

    # was a little unsure of what to put in the except block here
    def list(self, request):
        """Handle GET requests to Users resource
        Returns:
            Response -- JSON serialized list of Users
        """
        try:
            users = User.objects.all()
            serializer = UserSerializer(users, many=True, context={'request': request})
            return Response(serializer.data)    
            
        except User.DoesNotExist:
            pass