from rest_framework import viewsets
from .models import BudgetMethod
from .serializers import BudgetMethodSerializer

# Create your views here.

class BudgetMethodViewSet(viewsets.ModelViewSet):
    queryset = BudgetMethod.objects.all()
    serializer_class = BudgetMethodSerializers  