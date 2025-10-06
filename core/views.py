
# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
# from django.contrib import messages
# from django.contrib.auth.decorators import login_required
# from django.core.mail import send_mail
# from django.conf import settings
# import random
# from .models import CustomUser

# # ----------------------------
# # Home
# # ----------------------------
# def home(request):
#     return render(request, 'core/home.html')


# # ----------------------------
# # Registration
# # ----------------------------
# def register_view(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         confirm_password = request.POST.get('confirm_password')

#         if password != confirm_password:
#             messages.error(request, "Passwords do not match")
#             return redirect('register')

#         if CustomUser.objects.filter(email=email).exists():
#             messages.error(request, "Email already registered")
#             return redirect('register')

#         user = CustomUser(username=username, email=email)
#         user.set_password(password)
#         user.save()

#         messages.success(request, "Registration successful. Please login.")
#         return redirect('login')

#     return render(request, 'core/register.html')


# # ----------------------------
# # Login
# # ----------------------------
# def login_view(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         user = authenticate(request, email=email, password=password)  # Ensure email backend is configured
#         if user:
#             login(request, user)
#             messages.success(request, f"Welcome back, {user.username}!")
#             return redirect('dashboard')
#         else:
#             messages.error(request, "Invalid credentials")
#             return redirect('login')
#     return render(request, 'core/login.html')


# # ----------------------------
# # Logout
# # ----------------------------
# def logout_view(request):
#     logout(request)
#     messages.success(request, "Logged out successfully")
#     return redirect('home')


# # ----------------------------
# # Dashboard & AI Pages
# # ----------------------------
# @login_required
# def dashboard_view(request):
#     return render(request, 'core/dashboard.html')


# @login_required
# def ai_fitness_chatbot_view(request):
#     return render(request, 'core/ai_fitness_chatbot.html')


# @login_required
# def ai_nutrition_planner_view(request):
#     return render(request, 'core/ai_nutrition_planner.html')


# @login_required
# def accountability_dashboard_view(request):
#     data = {
#         'workouts_completed': 12,
#         'calories_burned': 3400,
#         'nutrition_score': 85
#     }
#     return render(request, 'core/accountability_dashboard.html', {'data': data})


# @login_required
# def analytics_dashboard_view(request):
#     return render(request, 'core/analytics_dashboard.html')


# # ----------------------------
# # Forgot Password Flow
# # ----------------------------
# def forgot_password_view(request):
#     if request.method == "POST":
#         email = request.POST.get('email')
#         try:
#             user = CustomUser.objects.get(email=email)
#             otp = random.randint(100000, 999999)
#             request.session['reset_otp'] = otp
#             request.session['reset_email'] = email

#             send_mail(
#                 "FitFare Password Reset OTP",
#                 f"Your password reset OTP is: {otp}",
#                 settings.DEFAULT_FROM_EMAIL,
#                 [email],
#                 fail_silently=False,
#             )

#             messages.success(request, "OTP sent to your email!")
#             return redirect('forgot_verify_otp')

#         except CustomUser.DoesNotExist:
#             messages.error(request, "Email not found!")
#             return redirect('forgot_password')

#     return render(request, 'core/forgot_password.html')


# def forgot_verify_otp_view(request):
#     """Step 2: Verify OTP entered by the user"""
#     if request.method == "POST":
#         user_otp = request.POST.get("otp")
#         session_otp = request.session.get("reset_otp")

#         if str(user_otp) == str(session_otp):
#             # Set flag to allow password reset
#             request.session['otp_verified'] = True
#             messages.success(request, "OTP verified successfully! Please reset your password.")
#             return redirect('reset_password')
#         else:
#             messages.error(request, "Invalid OTP. Please try again.")
#             return redirect('forgot_verify_otp')

#     return render(request, "core/forgot_verify_otp.html")


# def reset_password_view(request):
#     """Step 3: Allow the user to set a new password after OTP verification"""
#     # Ensure OTP was verified
#     if not request.session.get('otp_verified'):
#         messages.error(request, "You must verify OTP first!")
#         return redirect('forgot_password')

#     if request.method == "POST":
#         password = request.POST.get("password")
#         confirm_password = request.POST.get("confirm_password")

#         if password != confirm_password:
#             messages.error(request, "Passwords do not match.")
#             return render(request, "core/forgot_reset_password.html")

#         email = request.session.get("reset_email")
#         if email:
#             try:
#                 user = CustomUser.objects.get(email=email)
#                 user.set_password(password)
#                 user.save()

#                 request.session.flush()  # Clear all session data

#                 messages.success(request, "Password reset successfully! Please log in.")
#                 return redirect("login")

#             except CustomUser.DoesNotExist:
#                 messages.error(request, "User not found. Please try again.")
#                 return redirect('forgot_password')
#         else:
#             messages.error(request, "Session expired. Please try again.")
#             return redirect("forgot_password")

#     return render(request, "core/forgot_reset_password.html")
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
import random
from django.http import JsonResponse
from .models import CustomUser

# ---------------------------- Home ----------------------------
def home(request):
    return render(request, 'core/home.html')

# ---------------------------- Registration ----------------------------
def register_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('register')
        
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!")
            return redirect('register')
        
        # User create
        user = CustomUser.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        user.save()
        
        messages.success(request, "Registration successful! Please login.")
        return redirect('login')  # 🔹 Registration नंतर login page वर redirect
        
    return render(request, 'core/register.html')
# ---------------------------- Login ----------------------------
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('login')
    return render(request, 'core/login.html')

# ---------------------------- Logout ----------------------------
def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('home')

# ---------------------------- Dashboard & AI Pages ----------------------------
@login_required
def dashboard_view(request):
    return render(request, 'core/dashboard.html')

@login_required
def ai_fitness_chatbot_view(request):
    return render(request, 'core/ai_fitness_chatbot.html')

@login_required
def ai_nutrition_planner_view(request):
    return render(request, 'core/ai_nutrition_planner.html')

@login_required
def accountability_dashboard_view(request):
    data = {
        'workouts_completed': 12,
        'calories_burned': 3400,
        'nutrition_score': 85
    }
    return render(request, 'core/accountability_dashboard.html', {'data': data})

@login_required
def analytics_dashboard_view(request):
    return render(request, 'core/analytics_dashboard_view.html')

# ---------------------------- Forgot Password Flow ----------------------------
def forgot_password_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        try:
            user = CustomUser.objects.get(email=email)
            otp = random.randint(100000, 999999)
            request.session['reset_otp'] = otp
            request.session['reset_email'] = email

            send_mail(
                "FitFare Password Reset OTP",
                f"Your password reset OTP is: {otp}",
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )

            messages.success(request, "OTP sent to your email!")
            return redirect('forgot_verify_otp')

        except CustomUser.DoesNotExist:
            messages.error(request, "Email not found!")
            return redirect('forgot_password')

    return render(request, 'core/forgot_password.html')


def forgot_verify_otp_view(request):
    if request.method == "POST":
        user_otp = request.POST.get("otp")
        session_otp = request.session.get("reset_otp")

        if str(user_otp) == str(session_otp):
            request.session['otp_verified'] = True
            messages.success(request, "OTP verified successfully! Please reset your password.")
            return redirect('forgot_reset_password')  # <-- Use the correct URL name
        else:
            messages.error(request, "Invalid OTP. Please try again.")
            return redirect('forgot_verify_otp')

    return render(request, "core/forgot_verify_otp.html")


def reset_password_view(request):
    if not request.session.get('otp_verified'):
        messages.error(request, "You must verify OTP first!")
        return redirect('forgot_password')

    if request.method == "POST":
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, "core/forgot_reset_password.html")

        email = request.session.get("reset_email")
        if email:
            try:
                user = CustomUser.objects.get(email=email)
                user.set_password(password)
                user.save()

                # Clear session and redirect to login
                request.session.flush()
                messages.success(request, "Password reset successfully! Please log in.")
                return redirect("login")  # <-- हेच login page वर redirect करेल

            except CustomUser.DoesNotExist:
                messages.error(request, "User not found. Please try again.")
                return redirect('forgot_password')
        else:
            messages.error(request, "Session expired. Please try again.")
            return redirect("forgot_password")

    return render(request, "core/forgot_reset_password.html")


def dashboard_data_api(request):
    data = {
        "workouts_completed": 5,
        "calories_burned": 1200,
        "nutrition_score": 85,
        "streak_days": 3,
        "weekly_workouts": [1, 2, 1, 0, 3, 0, 2],
        "weekly_nutrition": [70, 75, 80, 85]
    }
    return JsonResponse(data)
