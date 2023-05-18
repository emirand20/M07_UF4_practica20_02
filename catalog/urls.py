from django.urls import path
from . import views

urlpatterns = [
    path('productos/', views.lista_productos, name='lista_productos'),
    path('productos/<int:pk>/', views.detalle_producto, name='detalle_producto'),
    path('productos/agregar/', views.agregar_producto, name='agregar_producto'),
    path('productos/<int:pk>/actualizar/', views.actualizar_producto, name='actualizar_producto'),
    path('productos/<int:pk>/eliminar/', views.eliminar_producto, name='eliminar_producto'),
]