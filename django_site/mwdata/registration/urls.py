from django.urls import path

from . import views


app_name = "registration"

urlpatterns = [
    path("", views.RegistrationCreate.as_view()),
    path(
        "confirmed/",
        views.RegistrationConfirm.as_view(),
        name="confirmed",
    ),
    path(
        "confirmation/<str:access_code>/",
        views.RegistrationAccepted.as_view(),
        name="registration_confirmation",
    ),
    path(
        "confirmation/<str:access_code>/done/",
        views.RegistrationAcceptedConfirm.as_view(),
        name="registration_confirmation_done",
    ),
]
