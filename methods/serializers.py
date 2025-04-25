from rest_framework import serializers
from .models import BudgetMethod


class BudgetMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = BudgetMethod
        fields = ['id', 'name', 'porcentaje_necesidad',
                  'porcentaje_deseos', 'porcenta_ahorros']
