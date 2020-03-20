"""Employees for SupplyMate"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
import sqlite3
from supplymateapi.models import Employee
from django.contrib.auth.models import User
from supplymateapi.views.user import UserSerializer
from supplymateapi.views.role import RoleSerializer

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for Employee
    Arguments:
        serializers
    """
    user = UserSerializer()
    role = RoleSerializer()

    class Meta:
        model = Employee
        url = serializers.HyperlinkedIdentityField(
            view_name='employee',
            lookup_field='id'
        )
        fields = ('id', 'user', 'role')
        depth = 2

class Employees(ViewSet):
    """Employees for SupplyMate"""

    def retrieve(self, request, pk=None):
        """Handle GET requests for single Employee
        Returns:
            Response -- JSON serialized Employee instance
        """
        try:
            employee = Employee.objects.get(pk=pk)
            serializer = EmployeeSerializer(employee, context={'request': request})
            return Response(serializer.data)

        except Exception as ex:
            return HttpResponseServerError(ex)

    # was a little unsure of what to put in the except block here
    def list(self, request):
        """Handle GET requests to Employees resource
        Returns:
            Response -- JSON serialized list of Employees
        """
        try:
            employees = Employee.objects.all()
            serializer = EmployeeSerializer(employees, many=True, context={'request': request})
            return Response(serializer.data)    
            
        except Employee.DoesNotExist:
            pass