from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponse


class AuthenticationRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if response.status_code == 403:
            return HttpResponse("You are UnAuthorized")
        return response
