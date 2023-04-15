from django.urls import path, include
from . import views

urlpatterns = [
    path("seller-login/", views.SellerLogin.as_view(), name="seller-login"),
    path(
        "seller-login/success/",
        views.SellerSuccessView.as_view(),
        name="seller-success",
    ),
    path("customer-login/", views.CustomerLogin.as_view(), name="customer-login"),
    path(
        "customer-login/success/",
        views.CustomerSuccessView.as_view(),
        name="customer-success",
    ),
    path("delivery-login/", views.DeliveryLogin.as_view(), name="delivery-login"),
    path(
        "delivery-login/success/",
        views.DeliverySuccessView.as_view(),
        name="delivery-success",
    ),
    path("signup/", views.SignupView.as_view(), name="onboard-user"),
]
