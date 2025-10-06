

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('login/', views.login_view, name='login'),
#     path('register/', views.register_view, name='register'),
#     path('logout/', views.logout_view, name='logout'),

#     # Forgot password + OTP flow
#     path('forgot-password/', views.forgot_password_view, name='forgot_password'),
#     path('forgot-password/verify-otp/', views.forgot_verify_otp_view, name='forgot_verify_otp'),
#     path('forgot-password/reset/', views.reset_password_view, name='forgot_reset_password'),

#     # Dashboards & AI Features
#     path('dashboard/', views.dashboard_view, name='dashboard'),
#     path('ai_fitness_chatbot/', views.ai_fitness_chatbot_view, name='ai_fitness_chatbot'),
#     path('ai_nutrition_planner/', views.ai_nutrition_planner_view, name='ai_nutrition_planner'),
#     path('accountability_dashboard/', views.accountability_dashboard_view, name='accountability_dashboard'),
#     path('analytics_dashboard_view/', views.analytics_dashboard_view, name='analytics_dashboard_view'),
# ]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),

    # AI Pages
    path('ai-fitness-chatbot/', views.ai_fitness_chatbot_view, name='ai_fitness_chatbot'),
    path('ai-nutrition-planner/', views.ai_nutrition_planner_view, name='ai_nutrition_planner'),
    path('accountability-dashboard/', views.accountability_dashboard_view, name='accountability_dashboard'),
    path('analytics-dashboard/', views.analytics_dashboard_view, name='analytics_dashboard'),

    # Forgot Password
    path('forgot-password/', views.forgot_password_view, name='forgot_password'),
    path('forgot-password/verify-otp/', views.forgot_verify_otp_view, name='forgot_verify_otp'),
    path('forgot-password/reset/', views.reset_password_view, name='forgot_reset_password'),
    path('api/dashboard-data/', views.dashboard_data_api, name='dashboard_data_api'),
]
