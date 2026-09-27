from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import AppointmentForm
from .models import Appointment
from doctors.models import Doctor


@login_required
def book_appointment(request):

    if request.method == "POST":
        form = AppointmentForm(request.POST)

        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = request.user
            appointment.save()

            return redirect("appointment_success")

    else:
        form = AppointmentForm()

    return render(
        request,
        "appointments/book_appointment.html",
        {
            "form": form
        }
    )


@login_required
def appointment_success(request):

    return render(
        request,
        "appointments/appointment_success.html"
    )


@login_required
def my_appointments(request):

    appointments = Appointment.objects.filter(
        patient=request.user
    ).select_related(
        "doctor",
        "doctor__user"
    ).order_by(
        "-appointment_date",
        "-appointment_time"
    )

    return render(
        request,
        "appointments/my_appointments.html",
        {
            "appointments": appointments
        }
    )


@login_required
def cancel_appointment(request, pk):

    appointment = Appointment.objects.filter(
        pk=pk,
        patient=request.user
    ).first()

    if (
        request.method == "POST"
        and appointment
        and appointment.status == Appointment.Status.PENDING
    ):
        appointment.status = Appointment.Status.CANCELLED
        appointment.save()

    return redirect("my_appointments")


@login_required
def doctor_appointments(request):

    doctor = Doctor.objects.filter(
        user=request.user
    ).first()

    if not doctor:
        return render(
            request,
            "appointments/not_a_doctor.html"
        )

    appointments = Appointment.objects.filter(
        doctor=doctor
    ).select_related(
        "patient"
    ).order_by(
        "appointment_date",
        "appointment_time"
    )

    return render(
        request,
        "appointments/doctor_appointments.html",
        {
            "appointments": appointments
        }
    )


@login_required
def confirm_appointment(request, pk):

    doctor = Doctor.objects.filter(
        user=request.user
    ).first()

    if not doctor:
        return redirect("doctor_appointments")

    appointment = Appointment.objects.filter(
        pk=pk,
        doctor=doctor
    ).first()

    if (
        request.method == "POST"
        and appointment
        and appointment.status == Appointment.Status.PENDING
    ):
        appointment.status = Appointment.Status.CONFIRMED
        appointment.save()

    return redirect("doctor_appointments")


@login_required
def complete_appointment(request, pk):

    doctor = Doctor.objects.filter(
        user=request.user
    ).first()

    if not doctor:
        return redirect("doctor_appointments")

    appointment = Appointment.objects.filter(
        pk=pk,
        doctor=doctor
    ).first()

    if (
        request.method == "POST"
        and appointment
        and appointment.status == Appointment.Status.CONFIRMED
    ):
        appointment.status = Appointment.Status.COMPLETED
        appointment.save()

    return redirect("doctor_appointments")

@login_required
def reject_appointment(request, pk):

    doctor = Doctor.objects.filter(
        user=request.user
    ).first()

    if not doctor:
        return redirect("doctor_appointments")

    appointment = Appointment.objects.filter(
        pk=pk,
        doctor=doctor
    ).first()

    if (
        request.method == "POST"
        and appointment
        and appointment.status == Appointment.Status.PENDING
    ):
        appointment.status = Appointment.Status.CANCELLED
        appointment.save()

    return redirect("doctor_appointments")