# from django.contrib.auth.backends import ModelBackend
# from .models import CustomUser

# class EmailBackend(ModelBackend):
#     def authenticate(self, request, username=None, password=None, **kwargs):
#         email = kwargs.get('email') or username
#         try:
#             user = CustomUser.objects.get(email=email)
#             if user.check_password(password):
#                 return user
#         except CustomUser.DoesNotExist:
#             return None

#     def get_user(self, user_id):
#         try:
#             return CustomUser.objects.get(pk=user_id)
#         except CustomUser.DoesNotExist:
#             return None
# core/backends.py
# from django.contrib.auth.backends import BaseBackend
# from django.contrib.auth import get_user_model

# User = get_user_model()

# class EmailBackend(BaseBackend):
#     def authenticate(self, request, email=None, password=None, **kwargs):
#         if not email or not password:
#             return None
#         try:
#             user = User.objects.get(email=email)
#             if user.check_password(password):
#                 return user
#         except User.DoesNotExist:
#             return None
#         return None

#     def get_user(self, user_id):
#         try:
#             return User.objects.get(pk=user_id)
#         except User.DoesNotExist:
#             return None
# core/backends.py
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model

User = get_user_model()

class EmailBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        if email is None or password is None:
            return None
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
