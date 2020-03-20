"""supplymate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib.auth.models import User
from supplymateapi.models import *
from supplymateapi.views import login_user, register_user, Items, ItemTypes, Addresses, Roles, SupplyRequests, Employees, Users, Statuses, SupplyRequestItems


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'items', Items, 'item')
router.register(r'itemtypes', ItemTypes, 'itemtype')
router.register(r'addresses', Addresses, 'address')
router.register(r'roles', Roles, 'role')
router.register(r'supplyrequests', SupplyRequests, 'supplyrequest')
router.register(r'supplyrequestitems', SupplyRequestItems, 'supplyrequestitem')
router.register(r'employees', Employees, 'employee')
router.register(r'users', Users, 'user')
router.register(r'statuses', Statuses, 'status')


urlpatterns = [
    path('', include(router.urls)),
    path('register', register_user),
    path('login', login_user),
    path('api-token-auth/', obtain_auth_token),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
