from django.contrib.sites import requests
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import NotFound, AuthenticationFailed
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import requests

from api.v1.dashboard.user.serializer import UserSerializer
from api.v1.mebel_sayt.category.services import ctg_format
from base.helper import BearerToken
from dashboard.models import User


class RegisterApi(GenericAPIView):

    def post(self, requests, *args, **kwargs):
        data = requests.data
        user = User()
        user.set_password(data.get("password"))
        user.name = data.get("name", "admin")
        user.user_name = data.get("user_name", "admin")
        user.phone = data.get("phone", "904991429")
        user.save()

        token = Token.objects.create(user)
        return Response({"token": token.key})


class UpdateUser(GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (BearerToken,)

    def put(self, requests, *args, **kwargs):

        data = requests.data
        serializer = self.serializer_class(data=data, instance=requests.user, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"success": "muaffaqiyatli"})


class LoginApi(GenericAPIView):
    def post(self, requests, *args, **kwargs):
        data = requests.data
        password = data.get("password")
        user_name = data.get("user_name")
        user = User.objects.filter(user_name=user_name).first()
        if not user:
            raise NotFound("User not found")
        if not user.check_password(password):
            raise AuthenticationFailed("Password incorrect")

        token = Token.objects.get(user=user)

        return Response({"token": token.key})
