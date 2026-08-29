from django.urls import path

from . import views


app_name = "accounts"


urlpatterns = [
    path(
        "register/",
        views.register,
        name="register"
    ),

    path(
        "login/",
        views.login_view,
        name="login"
    ),

    path(
        "logout/",
        views.logout_view,
        name="logout"
    ),

    path(
        "dashboard/",
        views.dashboard_redirect,
        name="dashboard_redirect"
    ),

    path(
    "citizen-dashboard/",
    views.citizen_dashboard,
    name="citizen_dashboard"
    ),

    path(
    "doctor-dashboard/",
    views.doctor_dashboard,
    name="doctor_dashboard"
    ),


]