from django.shortcuts import render
from .models import Foods  # , Notification
# , NotificationSerializer
from .serializer import FoodsSerializer, UserSerializer, RegisterSerializer
from rest_framework import status, filters, viewsets, generics  # , views
# from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed
# from django_filters.rest_framework import DjangoFilterBackend

import jwt
import datetime
# from django.core import import_export


# class Foods_veiwset(viewsets.ModelViewSet):
#     queryset = Foods.objects.all()
#     serializer_class = FoodsSerializer
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter]
#     filterset_fields = ['name']
#     search_fields = ['name']


class LoginView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        user = User.objects.filter(username=username).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')
        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret',
                           algorithm='HS256')
        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }
        return response


class UserView(APIView):

    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response


class RegisterView(generics.GenericAPIView):

    serializer_class = RegisterSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_data = serializer.data
        user = User.objects.get(email=user_data['email'])
        return Response(user_data, status=status.HTTP_201_CREATED)


class generics_list(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class generics_pk(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class generics_food_list(generics.ListAPIView):
    queryset = Foods.objects.all()
    serializer_class = FoodsSerializer


ACTIVITY_FACTORS = {
    "high": 1.75,
    "normal": 1.5,
    "low": 1.2,
}

GENDER_FACTOR = {"female": 1.2}  # Factor for females


class CalculateCalories(APIView):
    def post(self, request):
        try:
            weight = float(request.data["weight"])
            activity = request.data["activity"].lower()

            if activity not in ACTIVITY_FACTORS:
                return Response(
                    "Invalid activity level. Please enter 'High', 'Normal', or 'Low'.",
                    status=status.HTTP_400_BAD_REQUEST,
                )

            activity_factor = ACTIVITY_FACTORS[activity]
            gender_factor = GENDER_FACTOR.get(
                request.data["gender"].lower(), 1)

            calories = 24 * activity_factor * weight * gender_factor
            return Response(calories, status=status.HTTP_201_CREATED)

        except (ValueError, KeyError):
            return Response(
                "Invalid input. Please check data types and format.",
                status=status.HTTP_400_BAD_REQUEST,
            )