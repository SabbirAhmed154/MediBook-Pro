from django.shortcuts import render, redirect
from django.contrib.auth import login

from .forms import PatientRegisterForm

from doctors.models import Doctor
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):

    is_doctor = Doctor.objects.filter(
        user=request.user
    ).exists()

    return render(
        request,
        "accounts/dashboard.html",
        {
            "is_doctor": is_doctor
        }
    )
def patient_register(request):

    if request.method == "POST":

        form = PatientRegisterForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            return redirect("my_appointments")

    else:

        form = PatientRegisterForm()

    return render(
        request,
        "accounts/register.html",
        {
            "form": form
        }
    )

@login_required
def dashboard(request):

    is_doctor = Doctor.objects.filter(
        user=request.user
    ).exists()

    return render(
        request,
        "accounts/dashboard.html",
        {
            "is_doctor": is_doctor
        }
    )