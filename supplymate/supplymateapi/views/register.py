import json
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
from supplymateapi.models import Employee

@csrf_exempt
def register_user(request):
    '''Handles the creation of a new user for authentication
    Method arguments:
      request -- The full HTTP request object
    '''

    # Load the JSON string of the request body into a dict
    req_body = json.loads(request.body.decode())

    # Create a new user by invoking the `create_user` helper method
    # on Django's built-in User model
    new_user = User.objects.create_user(
        first_name=req_body['first_name'],
        last_name=req_body['last_name'],
        email=req_body['email'],
        username=req_body['username'],
        password=req_body['password'],
    )

    Employee.objects.create(
        role_id=1,
        user=new_user
    )

    # Use the REST Framework's token generator on the new user account
    token = Token.objects.create(user=new_user)

    # Return the token to the client
    data = json.dumps({"token": token.key})
    return HttpResponse(data, content_type='application/json')