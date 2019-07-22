from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Order(models.Model):
    CURRENCY_PLN = 'PLN'

    CURRENCY_TYPES = (
        (CURRENCY_PLN, 'Polski Złoty'),
    )

    user_driver = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='driver_orders')
    user_client = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='client_orders')
    priec = models.DecimalField(default=0.00, max_digits=8, decimal_places=2)
    currency = models.CharField(max_length=3, choices=CURRENCY_TYPES, default=CURRENCY_PLN)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_price(self):
        return f'{self.priec} {self.currency}'
