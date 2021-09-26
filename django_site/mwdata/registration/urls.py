from django.urls import path

from . import views


app_name = "registration"

urlpatterns = [
    path("", views.RegistrationCreate.as_view()),
    path(
        "python-week-of-code/",
        views.RegistrationWeek1Create.as_view(),
        name="registration-week1",
    ),
    path(
        "python-week-of-code/confirmed/",
        views.RegistrationConfirm.as_view(),
        name="confirmed-week1",
    ),
    path(
        "confirmed/",
        views.RegistrationConfirm.as_view(),
        name="confirmed",
    ),
    path(
        "confirmation/<str:access_code>/",
        views.RegistrationAccepted.as_view(),
        name="confirmation",
    ),
    path(
        "confirmation/<str:access_code>/done/",
        views.RegistrationAcceptedConfirm.as_view(),
        name="confirmation-done",
    ),
    path(
        "python-week-of-code/confirmation/<str:access_code>/",
        views.RegistrationWeek1Accepted.as_view(),
        name="week1-confirmation",
    ),
    path(
        "python-week-of-code/confirmation/<str:access_code>/done/",
        views.RegistrationWeek1AcceptedConfirm.as_view(),
        name="week1-confirmation-done",
    ),
]
