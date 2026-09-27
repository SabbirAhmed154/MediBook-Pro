from django.db import models
from django.conf import settings


class Doctor(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    specialization = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

    consultation_fee = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username