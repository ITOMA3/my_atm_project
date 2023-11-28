from django.db import models

class Account(models.Model):
    account_number = models.CharField(max_length=10)
    balance = models.DecimalField(max_digits=10,decimal_places=0)

        