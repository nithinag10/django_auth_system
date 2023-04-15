import jwt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .forms import LoginForm
from django.contrib.auth import authenticate
from django.shortcuts import render
from django.shortcuts import redirect
from .authenticate import CustomAuthentication
from datetime import timedelta, datetime
from assignment_ecommerce import settings
from .forms import CustomUserForm
from django.urls import reverse
from .permissions import IsCustomer, IsDelivery, IsSeller


class SignupView(APIView):
    def get(self, request):
        form = CustomUserForm()
        return render(request, "signup.html", {"form": form})

    def post(self, request):
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(user)
            token = jwt.encode(
                {
                    "user_info": {
                        "username": user.username,
                        "is_seller": user.is_seller,
                        "is_delivery": user.is_delivery,
                        "is_customer": user.is_customer,
                    },
                    "exp": datetime.utcnow() + timedelta(days=7),
                },
                settings.SECRET_KEY,
                algorithm="HS256",
            )
            response = redirect(reverse("home"))
            response.set_cookie(key="access_token", value=token, httponly=True)
            return response
        else:
            return render(request, "signup.html", {"form": form})


class EcommerceHome(APIView):
    def get(self, request):
        return render(request, "home.html")


class SellerLogin(APIView):
    def get(self, request):
        form = LoginForm()
        return render(request, "login.html", {"form": form, "place": "Seller"})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                token = jwt.encode(
                    {
                        "user_info": {
                            "username": user.username,
                            "is_seller": user.is_seller,
                            "is_delivery": user.is_delivery,
                            "is_customer": user.is_customer,
                        },
                        "exp": datetime.utcnow() + timedelta(days=7),
                    },
                    settings.SECRET_KEY,
                    algorithm="HS256",
                )
                response = redirect("success/")
                response.set_cookie("access_token", token, httponly=True)
                return response
            else:
                return Response(
                    {"detail": "Invalid login credentials"},
                    status=status.HTTP_401_UNAUTHORIZED,
                )
        else:
            return Response(
                {"detail": "Invalid form data"}, status=status.HTTP_400_BAD_REQUEST
            )


class DeliveryLogin(APIView):
    def get(self, request):
        form = LoginForm()
        return render(request, "login.html", {"form": form, "place": "Delivery"})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                token = jwt.encode(
                    {
                        "user_info": {
                            "username": user.username,
                            "is_seller": user.is_seller,
                            "is_delivery": user.is_delivery,
                            "is_customer": user.is_customer,
                        },
                        "exp": datetime.utcnow() + timedelta(days=7),
                    },
                    settings.SECRET_KEY,
                    algorithm="HS256",
                )
                response = redirect("success/")
                response.set_cookie("access_token", token, httponly=True)
                return response
            else:
                return Response(
                    {"detail": "Invalid login credentials"},
                    status=status.HTTP_401_UNAUTHORIZED,
                )
        else:
            return Response(
                {"detail": "Invalid form data"}, status=status.HTTP_400_BAD_REQUEST
            )


class CustomerLogin(APIView):
    def get(self, request):
        form = LoginForm()
        return render(request, "login.html", {"form": form, "place": "Customer"})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                token = jwt.encode(
                    {
                        "user_info": {
                            "username": user.username,
                            "is_seller": user.is_seller,
                            "is_delivery": user.is_delivery,
                            "is_customer": user.is_customer,
                        },
                        "exp": datetime.utcnow() + timedelta(days=7),
                    },
                    settings.SECRET_KEY,
                    algorithm="HS256",
                )
                response = redirect("success/")
                response.set_cookie("access_token", token, httponly=True)
                return response
            else:
                return Response(
                    {"detail": "Invalid login credentials"},
                    status=status.HTTP_401_UNAUTHORIZED,
                )
        else:
            return Response(
                {"detail": "Invalid form data"}, status=status.HTTP_400_BAD_REQUEST
            )


class SellerSuccessView(APIView):
    authentication_classes = (CustomAuthentication,)
    permission_classes = (IsSeller,)

    def get(self, request):
        return render(request, "success.html", {"type": "Seller"})


class DeliverySuccessView(APIView):
    authentication_classes = (CustomAuthentication,)
    permission_classes = (IsDelivery,)

    def get(self, request):
        return render(request, "success.html", {"type": "Delivery"})


class CustomerSuccessView(APIView):
    authentication_classes = (CustomAuthentication,)
    permission_classes = (IsCustomer,)

    def get(self, request):
        return render(request, "success.html", {"type": "Customer"})
