from rest_framework import authentication
from django.conf import settings
import jwt
from rest_framework.authentication import CSRFCheck
from django.contrib.auth import get_user_model
from rest_framework.exceptions import PermissionDenied


def enforce_csrf(request):
    check = CSRFCheck()
    check.process_request(request)
    reason = check.process_view(request, None, (), {})
    if reason:
        raise PermissionDenied("CSRF Failed: %s" % reason)


class CustomAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth_token = request.COOKIES.get("access_token")
        if not auth_token:
            raise PermissionDenied("There is no token present")
        try:
            # decode the JWT token and extract the user information
            decoded = jwt.decode(auth_token, settings.SECRET_KEY, algorithms=["HS256"])
            user_info = decoded["user_info"]

            # create a User object with the user information from the token
            user_model = get_user_model()
            user = user_model(**user_info)
            return user, user_info
        except (
            jwt.exceptions.InvalidSignatureError,
            jwt.exceptions.DecodeError,
            KeyError,
        ):
            # if the token is invalid or the user information is missing, return None
            raise PermissionDenied("Invalid Token")
