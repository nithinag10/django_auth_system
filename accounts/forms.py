from django import forms
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


User = get_user_model()


class CustomUserForm(UserCreationForm):
    is_customer = forms.BooleanField(required=False, initial=True)
    is_seller = forms.BooleanField(required=False)
    is_delivery = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2",
            "is_customer",
            "is_seller",
            "is_delivery",
        )
        labels = {
            "username": ("Username"),
            "email": ("Email"),
            "password1": ("Password"),
            "password2": ("Confirm password"),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_customer = self.cleaned_data.get("is_customer", False)
        user.is_seller = self.cleaned_data.get("is_seller", False)
        user.is_delivery = self.cleaned_data.get("is_delivery", False)
        if commit:
            user.save()
        return user
