from django.db import models

"""
    Payload:
        {
            "exp_date": "02/2026",
            "holder": "Fulano",
            "number": "0000000000000001",
            "cvv": "123",
        }
"""


class CreditCard(models.Model):
    exp_date = models.DateField()
    holder = models.CharField(max_length=100)
    number = models.CharField(max_length=16)
    cvv = models.CharField(max_length=4)

    def __str__(self):
        return self.holder
