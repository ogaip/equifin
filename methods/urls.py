from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BudgetMethodViewSet

router = DefaultRouter()
router.register(r'metodos', BudgetMethodViewSet)

urlpatterns = [
    path('', include(router.urls)),
]