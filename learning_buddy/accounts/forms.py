from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate
from .models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]


class LoginForm(forms.ModelForm):
    def clean(self):
        username = self.cleaned_data["username"]
        password = self.cleaned_data["password"]
        user = authenticate(username=username, password=password)

        if not user or not user.is_active:
            msg = "username or password does not exist"
            self.add_error("password", msg)
        return self.cleaned_data

    class Meta:
        model = User
        fields = ["username", "password"]
        widgets = {
            "username": forms.TextInput(attrs={"class":"login_field", "placeholder":"Username"}),
            "password": forms.PasswordInput(attrs={"minlength":"8", "class":"login_field", "placeholder":"Password" })
        }