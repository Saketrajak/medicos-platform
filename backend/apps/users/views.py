from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from .models import User
from .serializers import UserSerializer


@api_view(['POST'])
def register_user(request):

    data = request.data

    user = User.objects.create(
        username=data['username'],
        email=data['email'],
        password=make_password(data['password']),
        role='customer'
    )

    serializer = UserSerializer(user)

    return Response(serializer.data)



from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


@api_view(['POST'])
def login_user(request):

    username = request.data['username']
    password = request.data['password']

    user = authenticate(username=username, password=password)

    if user is not None:

        refresh = RefreshToken.for_user(user)

        return Response({
            "token": str(refresh.access_token),
            "role": user.role
        })

    return Response({"error": "Invalid credentials"})