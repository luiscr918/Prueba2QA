from django.urls import path
from .views import lista_razas, detalle_raza

urlpatterns = [
    path('', lista_razas, name='lista_razas'),
    path('raza/<int:raza_id>/', detalle_raza, name='detalle_raza'),
]