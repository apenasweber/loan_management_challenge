from django.core.exceptions import ValidationError
from django.db import models


def validate_cpf(value):
    if not str(value).isdigit():
        raise ValidationError("CPF deve conter apenas números.")


class Proposal(models.Model):
    STATUS_CHOICES = [
        ("P", "Pending"),
        ("A", "Approved"),
        ("R", "Rejected"),
    ]

    full_name = models.CharField(max_length=255)
    cpf = models.BigIntegerField(validators=[validate_cpf])
    address = models.CharField(max_length=255)
    loan_value = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default="P",
        editable=False,  # Impede a edição do campo no Django Admin
    )

    def __str__(self):
        return self.full_name
