# from django import forms
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from .models import CustomUser

# class RegisterForm(UserCreationForm):
#     email = forms.EmailField(required=True)

#     class Meta:
#         model = CustomUser
#         fields = ['username', 'email', 'password1', 'password2']

# class LoginForm(AuthenticationForm):
#     username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class OTPVerifyForm(forms.Form):
    otp = forms.CharField(max_length=6, required=True)


class ResetPasswordForm(forms.Form):
    new_password = forms.CharField(widget=forms.PasswordInput, required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput, required=True)
