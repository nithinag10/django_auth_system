from rest_framework.permissions import BasePermission
import jwt
from assignment_ecommerce import settings


class IsCustomer(BasePermission):
    """
    Allows access only to customers.
    """

    def has_permission(self, request, view):
        auth_token = request.COOKIES.get("access_token")
        decoded = jwt.decode(auth_token, settings.SECRET_KEY, algorithms=["HS256"])
        user_info = decoded["user_info"]
        if user_info["is_customer"] is False:
            return False
        return True


class IsDelivery(BasePermission):
    """
    Allows access only to Delivery
    """

    def has_permission(self, request, view):
        auth_token = request.COOKIES.get("access_token")
        decoded = jwt.decode(auth_token, settings.SECRET_KEY, algorithms=["HS256"])
        user_info = decoded["user_info"]
        if user_info["is_delivery"] is False:
            return False
        return True


class IsSeller(BasePermission):
    """
    Allows access only to Seller
    """

    def has_permission(self, request, view):
        auth_token = request.COOKIES.get("access_token")
        decoded = jwt.decode(auth_token, settings.SECRET_KEY, algorithms=["HS256"])
        user_info = decoded["user_info"]
        if user_info["is_seller"] is False:
            return False
        return True
