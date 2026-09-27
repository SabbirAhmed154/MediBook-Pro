from django import forms
from django.utils import timezone

from .models import Appointment
from doctors.models import Doctor


class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment

        fields = [
            "doctor",
            "appointment_date",
            "appointment_time",
            "reason",
        ]

        widgets = {
            "appointment_date": forms.DateInput(
                attrs={"type": "date"}
            ),

            "appointment_time": forms.TimeInput(
                attrs={"type": "time"}
            ),

            "reason": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "Why do you want to see the doctor?"
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["doctor"].queryset = Doctor.objects.filter(
            is_available=True
        )

    def clean(self):

        cleaned_data = super().clean()

        doctor = cleaned_data.get("doctor")
        appointment_date = cleaned_data.get("appointment_date")
        appointment_time = cleaned_data.get("appointment_time")

        today = timezone.localdate()
        current_time = timezone.localtime().time()

        if appointment_date and appointment_date < today:
            raise forms.ValidationError(
                "You cannot book an appointment in the past."
            )

        if (
            appointment_date
            and appointment_time
            and appointment_date == today
            and appointment_time <= current_time
        ):
            raise forms.ValidationError(
                "You cannot book an appointment for a past time."
            )

        if doctor and appointment_date and appointment_time:

            already_booked = Appointment.objects.filter(
                doctor=doctor,
                appointment_date=appointment_date,
                appointment_time=appointment_time
            ).exclude(
                status=Appointment.Status.CANCELLED
            ).exists()

            if already_booked:
                raise forms.ValidationError(
                    "This doctor is already booked at this date and time."
                )

        return cleaned_data