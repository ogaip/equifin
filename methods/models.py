from django.db import models

# Create your models here.

class BudgetMethod(models.Model):
    """
    Model representing a budget method.
    """
    name = models.CharField(max_length=100, unique=True)
    porcentaje_necesidad = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    porcentaje_deseos = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    porcenta_ahorros = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)

    def __str__(self):
        return f"{self.name} ({self.porcentaje_necesidad}%, {self.porcentaje_deseos}%, {self.porcenta_ahorros}%)"