from django.urls import path

from .views import (
    book_appointment,
    appointment_success,
    my_appointments,
    cancel_appointment,
    doctor_appointments,
    confirm_appointment,
    reject_appointment,
    complete_appointment,
)

urlpatterns = [
    path(
        "book/",
        book_appointment,
        name="book_appointment"
    ),

    path(
        "success/",
        appointment_success,
        name="appointment_success"
    ),

    path(
        "my/",
        my_appointments,
        name="my_appointments"
    ),

    path(
        "cancel/<int:pk>/",
        cancel_appointment,
        name="cancel_appointment"
    ),

    path(
        "doctor/",
        doctor_appointments,
        name="doctor_appointments"
    ),

    path(
        "confirm/<int:pk>/",
        confirm_appointment,
        name="confirm_appointment"
    ),

    path(
        "reject/<int:pk>/",
        reject_appointment,
        name="reject_appointment"
    ),

    path(
        "complete/<int:pk>/",
        complete_appointment,
        name="complete_appointment"
    ),
]